# coding=utf-8
"""
Author:song
"""
from pyecharts.charts import Bar, Line

bar = Bar()
bar.add_xaxis(["a", "b", "c", "d", "e"])
bar.add_yaxis("demo", [4300, 558, 120, 848, 21244])
bar.add_yaxis("demo2", [430, 1558, 4120, 1848, 2244])
bar.add_yaxis("demo3", [5300, 2558, 5120, 2848, 2144])
bar.add_yaxis("demo4", [6300, 3558, 6120, 3848, 2124])
bar.render("demo.html")