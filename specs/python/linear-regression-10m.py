from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Linear Regression 10M",
    "description": "A linear regression plot predicting flight arrival delay based on the time of departure, over 10 million flight records. Regression computation is performed in the database, with optimized selection updates using data cube indexes. The area around a regression line shows a 95% confidence interval. Select a region to view regression results for a data subset.\n"
  },
  "data": {
    "flights10m": {
      "type": "table",
      "query": "SELECT GREATEST(-60, LEAST(ARR_DELAY, 180))::DOUBLE AS delay, DISTANCE AS distance, DEP_TIME AS time FROM 'https://idl.uw.edu/mosaic-datasets/data/flights-10m.parquet'"
    }
  },
  "params": {
    "query": {
      "select": "intersect"
    }
  },
  "plot": [
    {
      "mark": "raster",
      "data": {
        "from": "flights10m"
      },
      "x": "time",
      "y": "delay",
      "pixelSize": 4,
      "pad": 0,
      "imageRendering": "pixelated"
    },
    {
      "mark": "regressionY",
      "data": {
        "from": "flights10m"
      },
      "x": "time",
      "y": "delay",
      "stroke": "gray"
    },
    {
      "mark": "regressionY",
      "data": {
        "from": "flights10m",
        "filterBy": "$query"
      },
      "x": "time",
      "y": "delay",
      "stroke": "firebrick"
    },
    {
      "select": "intervalXY",
      "as": "$query",
      "brush": {
        "fillOpacity": 0,
        "stroke": "currentColor"
      }
    }
  ],
  "xDomain": [
    0,
    24
  ],
  "yDomain": [
    -60,
    180
  ],
  "colorScale": "symlog",
  "colorScheme": "blues"
}
