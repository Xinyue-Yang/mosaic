from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Seattle Temperatures",
    "description": "Historical monthly temperatures in Seattle, WA. The gray range shows the minimum and maximum recorded temperatures. The blue range shows the average lows and highs.\n"
  },
  "data": {
    "weather": {
      "type": "parquet",
      "file": "data/seattle-weather.parquet"
    }
  },
  "plot": [
    {
      "mark": "areaY",
      "data": {
        "from": "weather"
      },
      "x": {
        "dateMonth": "date"
      },
      "y1": {
        "max": "temp_max"
      },
      "y2": {
        "min": "temp_min"
      },
      "fill": "#ccc",
      "fillOpacity": 0.25,
      "curve": "monotone-x"
    },
    {
      "mark": "areaY",
      "data": {
        "from": "weather"
      },
      "x": {
        "dateMonth": "date"
      },
      "y1": {
        "avg": "temp_max"
      },
      "y2": {
        "avg": "temp_min"
      },
      "fill": "steelblue",
      "fillOpacity": 0.75,
      "curve": "monotone-x"
    },
    {
      "mark": "ruleY",
      "data": [
        15
      ],
      "strokeOpacity": 0.5,
      "strokeDasharray": "5 5"
    }
  ],
  "xTickFormat": "%b",
  "yLabel": "Temperature Range (°C)",
  "width": 680,
  "height": 300
}
