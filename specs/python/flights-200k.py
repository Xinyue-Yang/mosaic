from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Cross-Filter Flights (200k)",
    "description": "Histograms showing arrival delay, departure time, and distance flown for over 200,000 flights. Select a histogram region to cross-filter the charts. Each plot uses an `intervalX` interactor to populate a shared Selection with `crossfilter` resolution.\n"
  },
  "data": {
    "flights": {
      "type": "parquet",
      "file": "data/flights-200k.parquet"
    }
  },
  "params": {
    "brush": {
      "select": "crossfilter"
    }
  },
  "vconcat": [
    {
      "plot": [
        {
          "mark": "rectY",
          "data": {
            "from": "flights",
            "filterBy": "$brush"
          },
          "x": {
            "bin": "delay"
          },
          "y": {
            "count": ""
          },
          "fill": "steelblue",
          "inset": 0.5
        },
        {
          "select": "intervalX",
          "as": "$brush"
        }
      ],
      "xDomain": "Fixed",
      "yTickFormat": "s",
      "width": 600,
      "height": 200
    },
    {
      "plot": [
        {
          "mark": "rectY",
          "data": {
            "from": "flights",
            "filterBy": "$brush"
          },
          "x": {
            "bin": "time"
          },
          "y": {
            "count": ""
          },
          "fill": "steelblue",
          "inset": 0.5
        },
        {
          "select": "intervalX",
          "as": "$brush"
        }
      ],
      "xDomain": "Fixed",
      "yTickFormat": "s",
      "width": 600,
      "height": 200
    },
    {
      "plot": [
        {
          "mark": "rectY",
          "data": {
            "from": "flights",
            "filterBy": "$brush"
          },
          "x": {
            "bin": "distance"
          },
          "y": {
            "count": ""
          },
          "fill": "steelblue",
          "inset": 0.5
        },
        {
          "select": "intervalX",
          "as": "$brush"
        }
      ],
      "xDomain": "Fixed",
      "yTickFormat": "s",
      "width": 600,
      "height": 200
    }
  ]
}
