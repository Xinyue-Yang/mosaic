from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Airline Travelers",
    "description": "A labeled line chart comparing airport travelers in 2019 and 2020.",
    "credit": "Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-labeled-line-chart)."
  },
  "data": {
    "travelers": {
      "type": "parquet",
      "file": "data/travelers.parquet"
    },
    "endpoint": {
      "type": "table",
      "query": "SELECT * FROM travelers ORDER BY date DESC LIMIT 1"
    }
  },
  "plot": [
    {
      "mark": "ruleY",
      "data": [
        0
      ]
    },
    {
      "mark": "lineY",
      "data": {
        "from": "travelers"
      },
      "x": "date",
      "y": "previous",
      "strokeOpacity": 0.35
    },
    {
      "mark": "lineY",
      "data": {
        "from": "travelers"
      },
      "x": "date",
      "y": "current"
    },
    {
      "mark": "text",
      "data": {
        "from": "endpoint"
      },
      "x": "date",
      "y": "previous",
      "text": [
        "2019"
      ],
      "fillOpacity": 0.5,
      "lineAnchor": "bottom",
      "dy": -6
    },
    {
      "mark": "text",
      "data": {
        "from": "endpoint"
      },
      "x": "date",
      "y": "current",
      "text": [
        "2020"
      ],
      "lineAnchor": "top",
      "dy": 6
    }
  ],
  "yGrid": True,
  "yLabel": "↑ Travelers per day",
  "yTickFormat": "s"
}
