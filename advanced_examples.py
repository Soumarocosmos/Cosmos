"""
Advanced Example: Multiple Chart Styles and Customizations
Demonstrates various ways to customize PieDrilldown charts.
"""
from piedrilldown import PieDrilldown, bar_of_pie, pie_of_pie
import matplotlib.pyplot as plt

# Example 1: Energy Consumption (Bar of Pie)
print("Creating Example 1: Energy Consumption...")
energy_chart = PieDrilldown(
    main_labels=['Oil', 'Gas', 'Coal', 'Renewables', 'Nuclear'],
    main_values=[39, 23, 19, 17, 2],
    drilldown_labels=['Bioenergy', 'Hydro', 'Solar', 'Wind', 'Geothermal'],
    drilldown_values=[12, 3, 1, 1, 0],
    drilldown_index=3,
    main_colors=['#4a4a4a', '#a67c52', '#c4a35a', '#5b9e4d', '#f0e68c'],
    drilldown_colors=['#2e7d32', '#42a5f5', '#fdd835', '#90caf9', '#e0e0e0']
)
energy_chart.plot(
    drilldown_type='bar',
    title='Gross final energy consumption in 2019',
    figsize=(12, 7),
    normalize_drilldown=False  # Show raw percentages
)
energy_chart.save('energy_bar_of_pie.png', dpi=150)

# Example 2: Market Share (Pie of Pie)
print("Creating Example 2: Market Share...")
market_chart = PieDrilldown(
    main_labels=['Company A', 'Company B', 'Company C', 'Others'],
    main_values=[35, 28, 22, 15],
    drilldown_labels=['Startup X', 'Startup Y', 'Startup Z', 'Rest'],
    drilldown_values=[5, 4, 3, 3],
    drilldown_index=3,
    main_colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
    drilldown_colors=['#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
)
market_chart.plot(
    drilldown_type='pie',
    title='Market Share Analysis',
    figsize=(13, 7),
    normalize_drilldown=True  # Normalize to 100%
)
market_chart.save('market_pie_of_pie.png', dpi=150)

# Example 3: Budget Breakdown with Normalized Percentages
print("Creating Example 3: Budget Breakdown...")
budget_chart = PieDrilldown(
    main_labels=['Salaries', 'Operations', 'Marketing', 'R&D', 'Other'],
    main_values=[45, 20, 15, 12, 8],
    drilldown_labels=['Social Media', 'Print', 'Events', 'Digital Ads'],
    drilldown_values=[6, 3, 4, 2],
    drilldown_index=2,  # Drill down on Marketing
    main_colors=['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51'],
    drilldown_colors=['#023e8a', '#0077b6', '#0096c7', '#00b4d8']
)
budget_chart.plot(
    drilldown_type='bar',
    title='Company Budget 2024 - Marketing Breakdown',
    figsize=(12, 7),
    normalize_drilldown=True,
    connection_color='#555555',
    connection_width=2.5
)
budget_chart.save('budget_breakdown.png', dpi=150)

# Example 4: Using convenience functions
print("Creating Example 4: Quick Charts...")
quick_chart = bar_of_pie(
    main_labels=['A', 'B', 'C', 'D'],
    main_values=[40, 30, 20, 10],
    drilldown_labels=['D1', 'D2', 'D3'],
    drilldown_values=[5, 3, 2],
    drilldown_index=3,
    title='Quick Bar of Pie Example'
)
quick_chart.save('quick_bar_of_pie.png', dpi=150)

print("\nAll examples created successfully!")
print("Generated files:")
print("  - energy_bar_of_pie.png")
print("  - market_pie_of_pie.png")
print("  - budget_breakdown.png")
print("  - quick_bar_of_pie.png")
