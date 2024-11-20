from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Cross-Filter Flights (10M)",
    "description": "Histograms showing arrival delay, departure time, and distance flown for 10 million flights.\nOnce loaded, automatically-generated indexes enable efficient cross-filtered selections.\n\n_You may need to wait a few seconds for the dataset to load._\n"
  },
  "data": {
    "flights10m": {
      "type": "table",
      "query": "SELECT GREATEST(-60, LEAST(ARR_DELAY, 180))::DOUBLE AS delay, DISTANCE AS distance, DEP_TIME AS time FROM 'https://idl.uw.edu/mosaic-datasets/data/flights-10m.parquet'"
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
            "from": "flights10m",
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
      "marginLeft": 75,
      "width": 600,
      "height": 200
    },
    {
      "plot": [
        {
          "mark": "rectY",
          "data": {
            "from": "flights10m",
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
      "marginLeft": 75,
      "width": 600,
      "height": 200
    },
    {
      "plot": [
        {
          "mark": "rectY",
          "data": {
            "from": "flights10m",
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
      "marginLeft": 75,
      "width": 600,
      "height": 200
    }
  ]
}
