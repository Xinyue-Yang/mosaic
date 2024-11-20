from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Pan & Zoom",
    "description": "Linked panning and zooming across plots: drag to pan, scroll to zoom. `panZoom` interactors update a set of bound selections, one per unique axis.\n"
  },
  "data": {
    "penguins": {
      "type": "parquet",
      "file": "data/penguins.parquet"
    }
  },
  "params": {
    "xs": {
      "select": "intersect"
    },
    "ys": {
      "select": "intersect"
    },
    "zs": {
      "select": "intersect"
    },
    "ws": {
      "select": "intersect"
    }
  },
  "hconcat": [
    {
      "vconcat": [
        {
          "plot": [
            {
              "mark": "frame"
            },
            {
              "mark": "dot",
              "data": {
                "from": "penguins"
              },
              "x": "bill_length",
              "y": "bill_depth",
              "fill": "species",
              "r": 2,
              "clip": True
            },
            {
              "select": "panZoom",
              "x": "$xs",
              "y": "$ys"
            }
          ],
          "width": 320,
          "height": 240
        },
        {
          "vspace": 10
        },
        {
          "plot": [
            {
              "mark": "frame"
            },
            {
              "mark": "dot",
              "data": {
                "from": "penguins"
              },
              "x": "bill_length",
              "y": "flipper_length",
              "fill": "species",
              "r": 2,
              "clip": True
            },
            {
              "select": "panZoom",
              "x": "$xs",
              "y": "$zs"
            }
          ],
          "width": 320,
          "height": 240
        }
      ]
    },
    {
      "hspace": 10
    },
    {
      "vconcat": [
        {
          "plot": [
            {
              "mark": "frame"
            },
            {
              "mark": "dot",
              "data": {
                "from": "penguins"
              },
              "x": "body_mass",
              "y": "bill_depth",
              "fill": "species",
              "r": 2,
              "clip": True
            },
            {
              "select": "panZoom",
              "x": "$ws",
              "y": "$ys"
            }
          ],
          "width": 320,
          "height": 240
        },
        {
          "vspace": 10
        },
        {
          "plot": [
            {
              "mark": "frame"
            },
            {
              "mark": "dot",
              "data": {
                "from": "penguins"
              },
              "x": "body_mass",
              "y": "flipper_length",
              "fill": "species",
              "r": 2,
              "clip": True
            },
            {
              "select": "panZoom",
              "x": "$ws",
              "y": "$zs"
            }
          ],
          "width": 320,
          "height": 240
        }
      ]
    }
  ]
}
