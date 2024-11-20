from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Sorted Bars",
    "description": "Sort and limit an aggregate bar chart of gold medals by country.\n"
  },
  "data": {
    "athletes": {
      "type": "parquet",
      "file": "data/athletes.parquet"
    }
  },
  "params": {
    "query": {
      "select": "intersect"
    }
  },
  "vconcat": [
    {
      "input": "menu",
      "label": "Sport",
      "as": "$query",
      "from": "athletes",
      "column": "sport",
      "value": "aquatics"
    },
    {
      "vspace": 10
    },
    {
      "plot": [
        {
          "mark": "barX",
          "data": {
            "from": "athletes",
            "filterBy": "$query"
          },
          "x": {
            "sum": "gold"
          },
          "y": "nationality",
          "fill": "steelblue",
          "sort": {
            "y": "-x",
            "limit": 10
          }
        }
      ],
      "xLabel": "Gold Medals",
      "yLabel": "Nationality",
      "yLabelAnchor": "top",
      "marginTop": 15
    }
  ]
}
