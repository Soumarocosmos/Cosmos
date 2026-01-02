"""
Jupyter Notebook-style Examples for PieDrilldown
Run this file or copy cells into a Jupyter notebook.
"""

# %% [markdown]
# # PieDrilldown Examples
# 
# This notebook demonstrates how to create Bar-of-Pie and Pie-of-Pie charts
# using the `piedrilldown` package.

# %% Import the package
from piedrilldown import PieDrilldown, bar_of_pie, pie_of_pie
import matplotlib.pyplot as plt

# %% [markdown]
# ## Example 1: Energy Consumption (Bar of Pie)
# 
# This example recreates a BEFS/FAO-style energy consumption chart.

# %% Energy Chart
chart = PieDrilldown(
    main_labels=['Oil', 'Gas', 'Coal', 'Renewables', 'Nuclear'],
    main_values=[39, 23, 19, 17, 2],
    drilldown_labels=['Bioenergy', 'Hydro', 'Solar', 'Wind', 'Geothermal'],
    drilldown_values=[12, 3, 1, 1, 0],
    drilldown_index=3,
    main_colors=['#4a4a4a', '#a67c52', '#c4a35a', '#5b9e4d', '#f0e68c'],
    drilldown_colors=['#2e7d32', '#42a5f5', '#fdd835', '#90caf9', '#e0e0e0']
)

chart.plot(
    drilldown_type='bar',
    title='Gross final energy consumption in 2019',
    figsize=(12, 7)
)
plt.show()

# %% [markdown]
# ## Example 2: Pie of Pie Chart
# 
# Shows how to create a secondary pie chart for drill-down.

# %% Pie of Pie
chart2 = PieDrilldown(
    main_labels=['Product A', 'Product B', 'Product C', 'Others'],
    main_values=[45, 25, 20, 10],
    drilldown_labels=['Sub-product 1', 'Sub-product 2', 'Sub-product 3'],
    drilldown_values=[5, 3, 2],
    drilldown_index=3
)

chart2.plot(
    drilldown_type='pie',
    title='Product Sales with Others Breakdown',
    figsize=(13, 7),
    normalize_drilldown=True  # Makes drill-down percentages add to 100%
)
plt.show()

# %% [markdown]
# ## Example 3: Custom Colors and Styling

# %% Custom styling
chart3 = PieDrilldown(
    main_labels=['Revenue', 'Expenses', 'Investments', 'Savings'],
    main_values=[50, 25, 15, 10],
    drilldown_labels=['Equipment', 'Stocks', 'Bonds', 'Real Estate'],
    drilldown_values=[5, 4, 3, 3],
    drilldown_index=2,
    main_colors=['#00897b', '#f44336', '#ff9800', '#4caf50'],
    drilldown_colors=['#7c4dff', '#448aff', '#00bcd4', '#8bc34a']
)

chart3.plot(
    drilldown_type='bar',
    title='Financial Overview - Investment Breakdown',
    figsize=(12, 7),
    connection_color='#333',
    connection_width=2,
    explode_drilldown=True,
    explode_amount=0.08
)
plt.show()

# %% [markdown]
# ## Example 4: Using Convenience Functions
# 
# Quick way to create charts with `bar_of_pie()` and `pie_of_pie()` functions.

# %% Quick bar_of_pie
quick_bar = bar_of_pie(
    main_labels=['A', 'B', 'C', 'D'],
    main_values=[40, 30, 20, 10],
    drilldown_labels=['D1', 'D2', 'D3'],
    drilldown_values=[5, 3, 2],
    drilldown_index=3,
    title='Quick Bar of Pie'
)
plt.show()

# %% Quick pie_of_pie
quick_pie = pie_of_pie(
    main_labels=['X', 'Y', 'Z'],
    main_values=[60, 25, 15],
    drilldown_labels=['Z1', 'Z2', 'Z3', 'Z4'],
    drilldown_values=[6, 4, 3, 2],
    drilldown_index=2,
    title='Quick Pie of Pie'
)
plt.show()

# %% [markdown]
# ## Saving Charts
# 
# Use the `save()` method to export charts to files.

# %% Saving
chart = bar_of_pie(
    main_labels=['A', 'B', 'C'],
    main_values=[50, 30, 20],
    drilldown_labels=['C1', 'C2'],
    drilldown_values=[12, 8],
    drilldown_index=2,
    title='Chart to Save'
)
# chart.save('my_chart.png', dpi=300)  # Uncomment to save
print("Chart saved successfully!")
