from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Flights Density",
    "description": "Density `heatmap` and `contour` lines for 200,000+ flights by departure hour and arrival delay. The sliders adjust the smoothing (bandwidth) and number of contour thresholds.\n"
  },
  "data": {
    "flights": {
      "type": "parquet",
      "file": "data/flights-200k.parquet"
    }
  },
  "params": {
    "bandwidth": 7,
    "thresholds": 10
  },
  "vconcat": [
    {
      "hconcat": [
        {
          "input": "slider",
          "label": "Bandwidth (σ)",
          "as": "$bandwidth",
          "min": 1,
          "max": 100
        },
        {
          "input": "slider",
          "label": "Thresholds",
          "as": "$thresholds",
          "min": 2,
          "max": 20
        }
      ]
    },
    {
      "plot": [
        {
          "mark": "heatmap",
          "data": {
            "from": "flights"
          },
          "x": "time",
          "y": "delay",
          "fill": "density",
          "bandwidth": "$bandwidth"
        },
        {
          "mark": "contour",
          "data": {
            "from": "flights"
          },
          "x": "time",
          "y": "delay",
          "stroke": "white",
          "strokeOpacity": 0.5,
          "bandwidth": "$bandwidth",
          "thresholds": "$thresholds"
        }
      ],
      "colorScale": "symlog",
      "colorScheme": "ylgnbu",
      "xAxis": "top",
      "xLabelAnchor": "center",
      "xZero": True,
      "yAxis": "right",
      "yLabelAnchor": "center",
      "marginTop": 30,
      "marginLeft": 5,
      "marginRight": 40,
      "width": 700,
      "height": 500
    }
  ]
}
