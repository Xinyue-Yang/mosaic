import json
from typing import Any, Dict, List, Union, Final, Iterable, Iterator, Literal
import sys
import yaml
import argparse
import copy
import re
import textwrap
from dataclasses import dataclass
from itertools import chain
from pathlib import Path 
from urllib import request
import graphlib
from .utils import get_valid_identifier, get_key_by_value, get_dependencies

sys.path.insert(0, str(Path.cwd()))

SCHEMA_VERSION: Final = "v0.10.0"
SCHEMA_URL_TEMPLATE: Final = "https://raw.githubusercontent.com/uwdata/mosaic/refs/heads/main/docs/public/schema/{version}.json"

def schema_url(version: str = SCHEMA_VERSION) -> str:
    return SCHEMA_URL_TEMPLATE.format(version=version)

def download_schemafile(
    version: str, schemapath: Path, download: bool = False
) -> Path:
    url = schema_url(version=version)
    if download:
        request.urlretrieve(url, schemapath)
    elif not schemapath.exists():
        msg = f"Cannot skip download: {schemapath!s} does not exist"
        raise ValueError(msg)
    return schemapath

def generate_class(class_name: str, class_schema: Dict[str, Any]) -> str:

    # Define a list of primitive types
    # primitive_types = ['string', 'number', 'integer', 'boolean']
    class_name = get_valid_identifier(class_name)

    # Check if the schema defines a simple type (like string, number) without properties
    if 'type' in class_schema and 'properties' not in class_schema: #DISCUSS: Change this to not isinstance(class_schema, Iterable)
        #assert not isinstance(class_schema, Iterable)
        return f"class {class_name}:\n    def __init__(self):\n        pass\n"

    # Check for '$ref' and handle it
    if '$ref' in class_schema:
        ref_class_name = class_schema['$ref'].split('/')[-1]
        return f"\nclass {class_name}:\n    pass  # This is a reference to '{ref_class_name}'\n"


    if 'anyOf' in class_schema:
        return generate_any_of_class(class_name, class_schema['anyOf'])

    # Extract properties and required fields
    properties = class_schema.get('properties', {})
    required = class_schema.get('required', [])

    class_def = f"class {class_name}:\n"
    class_def += "    def __init__(self"

    # Generate __init__ method parameters
    optional_params = []

    # Ensuring all the property names are valid Python identifiers
    property_items = list(properties.items())
    for prop, prop_schema in property_items:
        valid_prop = get_valid_identifier(prop)
        if valid_prop != prop:
            properties.pop(prop)
            properties[valid_prop] = prop_schema

    for prop, prop_schema in properties.items():
        type_hint = get_type_hint(prop_schema)
        if prop in required:
            # Required parameters should not have default values
            class_def += f", {prop}: {type_hint}"
        else:
            # Ensure we add optional parameters last
            optional_params.append((prop, prop_schema))

    for prop, prop_schema in optional_params:
        # Optional parameters should have a default value of None
        class_def += f", {prop}: {type_hint} = None"


    class_def += "):\n"

    # Generate attribute assignments in __init__
    for prop in properties:
        class_def += f"        self.{prop} = {prop}\n"

    return class_def


def generate_any_of_class(class_name: str, any_of_schemas: List[Dict[str, Any]]) -> str:
    types = [get_type_hint(schema) for schema in any_of_schemas]
    type_union = "Union[" + ", ".join(types) + "]"

    class_def = f"class {class_name}:\n"
    class_def += f"    def __init__(self, value: {type_union}):\n"
    class_def += "        self.value = value\n"
    
    return class_def


    
def get_type_hint(prop_schema: Dict[str, Any]) -> str:
        """Get type hint for a property schema."""
        if 'type' in prop_schema:
            if prop_schema['type'] == 'string':
                return 'str'
            elif prop_schema['type'] == 'boolean':
                return 'bool'
            elif prop_schema['type'] == 'object':
                return 'Dict[str, Any]'
        elif 'anyOf' in prop_schema:
            types = [get_type_hint(option) for option in prop_schema['anyOf']]
            return f'Union[{", ".join(types)}]'
        elif '$ref' in prop_schema:
            ref_class_name = prop_schema['$ref'].split('/')[-1]
            return f'"{ref_class_name}"'  
        return 'Any'

def load_schema(schema_path: Path) -> dict:
    """Load a JSON schema from the specified path."""
    with schema_path.open(encoding="utf8") as f:
        return json.load(f)

def generate_schema_wrapper(schema_file: Path, output_file: Path) -> str:
    """Generate a schema wrapper for the given schema file."""
    rootschema = load_schema(schema_file)
    
    rootschema_definitions = rootschema.get("definitions", {})
    ts = graphlib.TopologicalSorter()
    
    # if not output_file.parent.exists():
    #     output_file.parent.mkdir(parents=True, exist_ok=True)

    for name, schema in rootschema_definitions.items():
        #print(name)
        dependencies = get_dependencies(schema)
        if dependencies:
            ts.add(name, *dependencies)
        else:
            ts.add(name)
    
    class_order = list(ts.static_order())

    definitions: Dict[str, str] = {}

    for name in class_order:
        schema = rootschema_definitions.get(name)
        class_code = generate_class(name, schema)
        definitions[name] = class_code

    generated_classes =  "\n\n".join(definitions.values())
    generated_classes = "from typing import Union, Dict, Any\n\n" + generated_classes
    #print(generated_classes)

    with open(output_file, 'w') as f:
        f.write(generated_classes)

def main():
    parser = argparse.ArgumentParser(
        prog="our_schema_generator", description="Generate the JSON schema for mosaic apps"
    )   
    parser.add_argument("schema_file", help="Path to the JSON schema file")

    parser.add_argument(
        "--download", action="store_true", help="download the schema"
    )   
    args = parser.parse_args()
    
    #vn = '.'.join(version.split(".")[:1]) #Not using this currently
    schemapath = Path(args.schema_file).resolve()
    schemapath = download_schemafile( 
        version=SCHEMA_VERSION,
        schemapath=schemapath,
        download = args.download
    )

    output_file = Path("packages/schema_wrapper/generated_classes.py")
    generate_schema_wrapper(schemapath, output_file)

# Main execution
if __name__ == "__main__":
    main()
