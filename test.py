#!/usr/bin/env python

import leather

dot_data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

line_data = [
    (0, 4),
    (1, 3),
    (2, 5),
    (5, 6),
    (9, 10)
]

chart = leather.Chart()
# chart.set_x_scale(leather.Linear(0, 20))
chart.add_dots(dot_data)
chart.add_lines(line_data)
chart.to_svg('test.svg')

# dot_data = [
#     ('foo', 3),
#     ('bing', 5),
#     ('baz', 9),
#     ('blurg', 4)
# ]
#
# line_data = [
#     ('foo', 7),
#     ('bing', 2),
#     ('baz', 3),
#     ('blurg', 4)
# ]
#
# chart = leather.Chart()
# chart.add_column(line_data)
# chart.add_dot(dot_data)
# chart.to_svg('test.svg')
#
# data = [[
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ], [
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ],[
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ]]
#
# grid = leather.Grid()
#
# chart = leather.Chart('Chart A')
# chart.add_lines(data[0])
# grid.add_chart(chart)
#
# chart = leather.Chart('Chart B')
# chart.add_dots(data[1])
# grid.add_chart(chart)
#
# chart = leather.Chart('Chart C')
# chart.add_dots(data[2])
# grid.add_chart(chart)
#
# grid.to_svg('test.svg')

# data = [[
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ], [
#     (0, 4),
#     (1, 3),
#     (2, 3),
#     (10, 7),
#     (15, 5)
# ], [
#     (0, 4),
#     (5, 5),
#     (6, 6),
#     (7, 7),
#     (8, 8)
# ], [
#     (4, 4),
#     (6, 3),
#     (7, 5),
#     (8, 6),
#     (12, 10)
# ]]
#
# lattice = leather.Lattice(data, leather.Lines('purple'), ['A', 'B', 'C', 'D'])
#
# lattice.to_svg('test.svg', 1200, 600)

# data = [
#     (3, 1),
#     (5, 3),
#     (9, 12),
#     (4, 15)
# ]
#
# chart = leather.Chart()
# chart.add_bars(data)
# chart.to_svg('test.svg')

# chart = leather.Chart()
# chart.set_x_scale(leather.Linear(0, 20))
# chart.set_x_axis(leather.Axis(ticks=5))
# chart.set_y_scale(leather.Linear(0, 20))
# chart.set_y_axis(leather.Axis(ticks=5))
# chart.add_dots(data)
#
# chart.to_svg('test.svg')
