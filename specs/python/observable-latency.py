from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Observable Latency",
    "description": "Web request latency on Observable.com.\nEach pixel in the heatmap shows the most common route (URL pattern) at a given response latency within a time interval.\nUse the bar chart of most-requested routes to filter the heatmap and isolate specific patterns.\nOr, select a range in the heatmap to show the corresponding most-requested routes.\n\n_You may need to wait a few seconds for the dataset to load._\n",
    "credit": "Adapted from an [Observable Framework example](https://observablehq.com/framework/examples/api/)."
  },
  "data": {
    "latency": {
      "type": "parquet",
      "file": "https://idl.uw.edu/mosaic-datasets/data/observable-latency.parquet"
    }
  },
  "params": {
    "filter": {
      "select": "crossfilter"
    },
    "highlight": {
      "select": "intersect"
    }
  },
  "vconcat": [
    {
      "plot": [
        {
          "mark": "frame",
          "fill": "black"
        },
        {
          "mark": "raster",
          "data": {
            "from": "latency",
            "filterBy": "$filter"
          },
          "x": "time",
          "y": "latency",
          "fill": {
            "argmax": [
              "route",
              "count"
            ]
          },
          "fillOpacity": {
            "sum": "count"
          },
          "width": 2016,
          "height": 500,
          "imageRendering": "pixelated"
        },
        {
          "select": "intervalXY",
          "as": "$filter"
        }
      ],
      "colorDomain": "Fixed",
      "colorScheme": "observable10",
      "opacityDomain": [
        0,
        25
      ],
      "opacityClamp": True,
      "yScale": "log",
      "yLabel": "↑ Duration (ms)",
      "yDomain": [
        0.5,
        10000
      ],
      "yTickFormat": "s",
      "xScale": "utc",
      "xLabel": None,
      "xDomain": [
        1706227200000,
        1706832000000
      ],
      "width": 680,
      "height": 300,
      "margins": {
        "left": 35,
        "top": 20,
        "bottom": 30,
        "right": 20
      }
    },
    {
      "plot": [
        {
          "mark": "barX",
          "data": {
            "from": "latency",
            "filterBy": "$filter"
          },
          "x": {
            "sum": "count"
          },
          "y": "route",
          "fill": "route",
          "sort": {
            "y": "-x",
            "limit": 15
          }
        },
        {
          "select": "toggleY",
          "as": "$filter"
        },
        {
          "select": "toggleY",
          "as": "$highlight"
        },
        {
          "select": "highlight",
          "by": "$highlight"
        }
      ],
      "colorDomain": "Fixed",
      "xLabel": "Routes by Total Requests",
      "xTickFormat": "s",
      "yLabel": None,
      "width": 680,
      "height": 300,
      "marginTop": 5,
      "marginLeft": 220,
      "marginBottom": 35
    }
  ]
}
