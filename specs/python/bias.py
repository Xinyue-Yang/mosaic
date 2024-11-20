from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Bias Parameter",
    "description": "Dynamically adjust queried values by adding a Param value. The SQL expression is re-computed in the database upon updates.\n"
  },
  "data": {
    "walk": {
      "type": "parquet",
      "file": "data/random-walk.parquet"
    }
  },
  "params": {
    "point": 0
  },
  "vconcat": [
    {
      "input": "slider",
      "label": "Bias",
      "as": "$point",
      "min": 1,
      "max": 1000,
      "step": 0.1
    },
    {
      "plot": [
        {
          "mark": "areaY",
          "data": {
            "from": "walk"
          },
          "x": "t",
          "y": {
            "sql": "v + $point"
          },
          "fill": "steelblue"
        }
      ],
      "width": 680,
      "height": 200
    }
  ]
}
