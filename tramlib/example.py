from nvd3 import lineWithFocusChart
# Open File to write the D3 Graph
output_file = open('test-nvd3.html', 'w')
chart = lineWithFocusChart(name='lineWithFocusChart', x_is_date=True, x_axis_format="%d %b %Y")
xdata = [1365026400000, 1365026500000, 1365026600000, 1365026700000, 1365026800000, 1365026900000, 1365027000000]
ydata = [-6, 5, -1, 2, 4, 8, 10]

extra_serie = {"tooltip": {"y_start": "", "y_end": " ext"},
               "date_format": "%d %b %Y"}
chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()