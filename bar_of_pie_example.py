"""
Example: Bar of Pie Chart - Energy Consumption
"""
from piedrilldown import PieDrilldown

# Create a bar-of-pie chart showing energy consumption breakdown
chart = PieDrilldown(
    main_labels=['Oil', 'Gas', 'Coal', 'Renewables', 'Nuclear'],
    main_values=[39, 23, 19, 17, 2],
    drilldown_labels=['Bioenergy', 'Hydro', 'Solar', 'Wind', 'Geothermal'],
    drilldown_values=[12, 3, 1, 1, 0],
    drilldown_index=3,  # Drill down on 'Renewables'
    main_colors=['#4a4a4a', '#a67c52', '#c4a35a', '#5b9e4d', '#f0e68c'],
    drilldown_colors=['#2e7d32', '#42a5f5', '#fdd835', '#90caf9', '#e0e0e0']
)

chart.plot(
    drilldown_type='bar',
    title='Gross final energy consumption in 2019',
    figsize=(12, 7)
)

chart.save('bar_of_pie_example.png', dpi=150)
chart.show()
