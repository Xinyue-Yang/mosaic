from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Mark Types",
    "description": "A subset of supported mark types.\n\n- Row 1: `barY`, `lineY`, `text`, `tickY`, `areaY`\n- Row 2: `regressionY`, `hexbin`, `contour`, `heatmap`, `denseLine`\n"
  },
  "data": {
    "md": {
      "type": "json",
      "data": [
        {
          "i": 0,
          "u": "A",
          "v": 2
        },
        {
          "i": 1,
          "u": "B",
          "v": 8
        },
        {
          "i": 2,
          "u": "C",
          "v": 3
        },
        {
          "i": 3,
          "u": "D",
          "v": 7
        },
        {
          "i": 4,
          "u": "E",
          "v": 5
        },
        {
          "i": 5,
          "u": "F",
          "v": 4
        },
        {
          "i": 6,
          "u": "G",
          "v": 6
        },
        {
          "i": 7,
          "u": "H",
          "v": 1
        }
      ]
    }
  },
  "plotDefaults": {
    "xAxis": None,
    "yAxis": None,
    "margins": {
      "left": 5,
      "top": 5,
      "right": 5,
      "bottom": 5
    },
    "width": 160,
    "height": 100,
    "yDomain": [
      0,
      9
    ]
  },
  "vconcat": [
    {
      "hconcat": [
        {
          "plot": [
            {
              "mark": "barY",
              "data": {
                "from": "md"
              },
              "x": "u",
              "y": "v",
              "fill": "steelblue"
            }
          ]
        },
        {
          "plot": [
            {
              "mark": "lineY",
              "data": {
                "from": "md"
              },
              "x": "u",
              "y": "v",
              "stroke": "steelblue",
              "curve": "monotone-x",
              "marker": "circle"
            }
          ]
        },
        {
          "plot": [
            {
              "mark": "text",
              "data": {
                "from": "md"
              },
              "x": "u",
              "y": "v",
              "text": "u",
              "fill": "steelblue"
            }
          ]
        },
        {
          "plot": [
            {
              "mark": "tickY",
              "data": {
                "from": "md"
              },
              "x": "u",
              "y": "v",
              "stroke": "steelblue"
            }
          ]
        },
        {
          "plot": [
            {
              "mark": "areaY",
              "data": {
                "from": "md"
              },
              "x": "u",
              "y": "v",
              "fill": "steelblue"
            }
          ]
        }
      ]
    },
    {
      "hconcat": [
        {
          "plot": [
            {
              "mark": "dot",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "fill": "currentColor",
              "r": 1.5
            },
            {
              "mark": "regressionY",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "stroke": "steelblue"
            }
          ],
          "xDomain": [
            -0.5,
            7.5
          ]
        },
        {
          "plot": [
            {
              "mark": "hexgrid",
              "stroke": "#aaa",
              "strokeOpacity": 0.5
            },
            {
              "mark": "hexbin",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "fill": {
                "count": ""
              }
            }
          ],
          "colorScheme": "blues",
          "xDomain": [
            -1,
            8
          ]
        },
        {
          "plot": [
            {
              "mark": "contour",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "stroke": "steelblue",
              "bandwidth": 15
            }
          ],
          "xDomain": [
            -1,
            8
          ]
        },
        {
          "plot": [
            {
              "mark": "heatmap",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "fill": "density",
              "bandwidth": 15
            }
          ],
          "colorScheme": "blues",
          "xDomain": [
            -1,
            8
          ]
        },
        {
          "plot": [
            {
              "mark": "denseLine",
              "data": {
                "from": "md"
              },
              "x": "i",
              "y": "v",
              "fill": "density",
              "bandwidth": 2,
              "pixelSize": 1
            }
          ],
          "colorScheme": "blues",
          "xDomain": [
            -1,
            8
          ]
        }
      ]
    }
  ]
}
