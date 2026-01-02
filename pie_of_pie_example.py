"""
Example: Pie of Pie Chart
"""
from piedrilldown import PieDrilldown

# Create a pie-of-pie chart
chart = PieDrilldown(
    main_labels=['Category A', 'Category B', 'Category C', 'Others'],
    main_values=[45, 25, 20, 10],
    drilldown_labels=['Sub 1', 'Sub 2', 'Sub 3', 'Sub 4'],
    drilldown_values=[4, 3, 2, 1],
    drilldown_index=3  # Drill down on 'Others'
)

chart.plot(
    drilldown_type='pie',
    title='Sales Distribution with Others Breakdown',
    figsize=(13, 7)
)

chart.save('pie_of_pie_example.png', dpi=150)
chart.show()
