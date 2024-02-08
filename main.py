import pandas as pd
from FileOperation import FileOperation
from SalesData import SalesData
import seaborn as sns
import matplotlib.pyplot as plt
# Create an instance of the FileOperation class
file_operation = FileOperation()

# Read data from a CSV file
csv_data = file_operation.read_csv("YafeNof.csv")
print("Data read from CSV file:")
print(csv_data)

# Save data to a new CSV file
data_to_save = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
file_operation.save_to_excel(data_to_save, "output.csv")

data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Sales': [100, 200, 150, 300, 250, 400, 200, 150, 300],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'May'],
    'Number of Selling': [10, 5, 8, 12, 3, 15, 7, 4, 9],
    'Price': [50, 100, 70, 120, 80, 130, 60, 110, 90],
    'Discount': [0.1, 0.2, 0.15, 0.1, 0.25, 0.1, 0.2, 0.15, 0.1],
    'Total': [1000, 1000, 1200, 1200, 750, 750, 1400, 1400, 1800],
    'Date': ['2022-01-01', '2022-01-05', '2022-02-03', '2022-02-10', '2022-03-15', '2022-03-20', '2022-04-25',
             '2022-04-27', '2022-05-30'],
    'CustomerId*Price': ['A*50', 'B*100', 'A*70', 'C*120', 'B*80', 'C*130', 'A*60', 'B*110', 'C*90']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create an instance of SalesData class
sales_data = SalesData(df)

# Call the methods
sales_data.eliminate_duplicates()
sales_data.calculate_cumulative_sales()
sales_data.add_90_percent_values_column()
sales_data.bar_chart_category_sum()
mean, median, second_max = sales_data.calculate_mean_quantity()
filtered_data = sales_data.filter_by_sellings_or_and()
sales_data.divide_by_2()
stats = sales_data.calculate_stats()
total_sales = sales_data.calculate_total_sales()
analysis_result = sales_data.analyze_sales_data()
additional_data = sales_data.add_additional_data()

# Print results
print("Mean:", mean)
print("Median:", median)
print("Second Max:", second_max)
print("Filtered Data:", filtered_data)
print("Statistics:", stats)
print("Total Sales:", total_sales)
print("Analysis Result:", analysis_result)
print("Additional Data:", additional_data)

# Task 4 examples
print("\nTask 4 Examples:")

# Example for method convert_date_format
sales_data.convert_date_format(['Date'])
print("\nAfter converting date format:")
print(sales_data.data)

# Example for method categorize_prices
sales_data.categorize_prices()
print("\nAfter categorizing prices:")
print(sales_data.data)

# Example for method change_index
sales_data.change_index()
print("\nAfter changing index:")
print(sales_data.data)

# Example for method split_and_concat
split_concatenated_df = sales_data.split_and_concat()
print("\nAfter splitting and concatenating:")
print(split_concatenated_df)

# Example for method complex_data_transformation
transformed_df = sales_data.complex_data_transformation()
print("\nAfter complex data transformation:")
print(transformed_df)

# Example for method group_with_function
grouped_data = sales_data.group_with_function('Month', 'Sales', sum)
print("\nGrouped data by month with sum of sales:")
print(grouped_data)

# Example for locating specific row by index
specific_row = sales_data.locate_specific_row_by_index(2)
print("\nSpecific row by index:")
print(specific_row)

# Example for locating specific row by index (alternative method)
specific_row_alt = sales_data.locate_specific_row_by_index_alternative(2)
print("\nSpecific row by index (alternative method):")
print(specific_row_alt)

# Example for locating specific column by label
specific_col_label = sales_data.locate_specific_column_by_label('Product')
print("\nSpecific column by label:")
print(specific_col_label)

# Example for locating specific column by index
specific_col_index = sales_data.locate_specific_column_by_index(2)
print("\nSpecific column by index:")
print(specific_col_index)

# Example for locating specific columns and rows
specific_cols_rows = sales_data.locate_specific_columns_and_rows([0, 1, 2], [3, 4, 5])
print("\nSpecific columns and rows:")
print(specific_cols_rows)

# Example for locating specific rows and columns
specific_rows_cols = sales_data.locate_specific_rows_and_columns([0, 1, 2], [3, 4, 5])
print("\nSpecific rows and columns:")
print(specific_rows_cols)

# Example for filtering by mask
filtered_df = sales_data.filter_by_mask([True, False, True, False, True, False, True, False, True])
print("\nFiltered dataframe by mask:")
print(filtered_df)


# Task 26: Handle data errors
sales_data.handle_data_errors()

# Task 27: Save modified sales data
sales_data.save_modified_sales_data()

# Task 28: Save figures
figures = [plt.figure(), sns.barplot(x='Product', y='Sales', data=sales_data.data)]
SalesData.save_figures("D:\\", figures)
