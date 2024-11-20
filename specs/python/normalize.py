from mosaic_spec import *
from typing import Dict, Any, Union

spec = {
  "meta": {
    "title": "Normalized Stock Prices",
    "description": "What is the return on investment for different days? Hover over the chart to normalize the stock prices for the percentage return on a given day. A `nearestX` interactor selects the nearest date, and parameterized expressions reactively update in response.\n"
  },
  "data": {
    "stocks": {
      "type": "parquet",
      "file": "data/stocks.parquet"
    },
    "labels": {
      "type": "table",
      "query": "SELECT MAX(Date) as Date, ARGMAX(Close, Date) AS Close, Symbol FROM stocks GROUP BY Symbol"
    }
  },
  "params": {
    "point": {
      "date": "2013-05-13"
    }
  },
  "plot": [
    {
      "mark": "ruleX",
      "x": "$point"
    },
    {
      "mark": "textX",
      "x": "$point",
      "text": "$point",
      "frameAnchor": "top",
      "lineAnchor": "bottom",
      "dy": -7
    },
    {
      "mark": "text",
      "data": {
        "from": "labels"
      },
      "x": "Date",
      "y": {
        "sql": "Close / (SELECT MAX(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
      },
      "dx": 2,
      "text": "Symbol",
      "fill": "Symbol",
      "textAnchor": "start"
    },
    {
      "mark": "lineY",
      "data": {
        "from": "stocks"
      },
      "x": "Date",
      "y": {
        "sql": "Close / (SELECT MAX(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
      },
      "stroke": "Symbol"
    },
    {
      "select": "nearestX",
      "as": "$point"
    }
  ],
  "yScale": "log",
  "yDomain": [
    0.2,
    6
  ],
  "yGrid": True,
  "xLabel": None,
  "yLabel": None,
  "yTickFormat": "%",
  "width": 680,
  "height": 400,
  "marginRight": 35
}
