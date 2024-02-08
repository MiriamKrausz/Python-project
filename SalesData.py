import numpy as np
import pandas as pd
import seaborn as sns
from typing import List
from FileOperation import FileOperation


class SalesData:

    # def __init__(self, data):
    #     self.data = data
    # def eliminate_duplicates(self):
    #     self.data.drop_duplicates(inplace=True)
    #
    # def add_90_percent_values_column(self):
    #     self.data['Discount90'] = self.data['Discount'] * 0.9
    #
    # def bar_chart_category_sum(self):
    #     sns.barplot(x='Product', y='Quantity', data=self.data.groupby('Product')['Quantity'].sum().reset_index())
    #
    # def calculate_mean_quantity(self):
    #     mean = np.mean(self.data['Total'])
    #     median = np.median(self.data['Total'])
    #     second_max = np.partition(self.data['Total'], -2)[-2]
    #     return mean, median, second_max
    #
    # def filter_by_sellings_or_and(self):
    #     filtered_data = self.data[((self.data['Number of Selling'] > 5) | (self.data['Number of Selling'] == 0))
    #                               & ((self.data['Price'] > 300) & (self.data['Number of Selling'] < 2))]
    #     return filtered_data
    #
    # def divide_by_2(self):
    #     self.data['BlackFridayPrice'] = self.data['Price'] / 2
    #
    # def calculate_stats(self, columns=None):
    #     if columns is None:
    #         columns = self.data.columns
    #     stats = {}
    #     for col in columns:
    #         stats[col] = {
    #             'max': self.data[col].max(),
    #             'sum': self.data[col].sum(),
    #             'abs_sum': np.abs(self.data[col]).sum(),
    #             'cum_max': self.data[col].cummax()
    #         }
    #     return stats
    #
    #
    #
    #
    #
    #
    # def calculate_total_sales(self):
    #     return self.data.groupby('Product')['Sales'].sum().to_dict()
    #
    # def _calculate_total_sales_per_month(self):
    #     return self.data.groupby('Month')['Sales'].sum().to_dict()
    #
    # def _identify_best_selling_product(self):
    #     total_sales = self.calculate_total_sales()
    #     return max(total_sales, key=total_sales.get)
    #
    # def _identify_month_with_highest_sales(self):
    #     total_sales_per_month = self._calculate_total_sales_per_month()
    #     return max(total_sales_per_month, key=total_sales_per_month.get)
    #
    # def analyze_sales_data(self):
    #     best_selling_product = self._identify_best_selling_product()
    #     month_with_highest_sales = self._identify_month_with_highest_sales()
    #     return {
    #         'best_selling_product': best_selling_product,
    #         'month_with_highest_sales': month_with_highest_sales
    #     }
    # def add_additional_data(self):
    #     total_sales = self.calculate_total_sales()
    #     minimest_selling_product = min(total_sales, key=total_sales.get)
    #     average_sales = sum(total_sales.values()) / len(total_sales)
    #     analysis_result = self.analyze_sales_data()
    #     analysis_result.update({
    #         'minimest_selling_product': minimest_selling_product,
    #         'average_sales': average_sales
    #     })
    #     return analysis_result

    # Example usage:
    def __init__(self, data):
        self.data = data

    # =======================task2=======================
    def eliminate_duplicates(self):
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)

    def calculate_total_sales(self):
        return self.data.groupby('Product')['Sales'].sum().to_dict()

    def _calculate_total_sales_per_month(self):
        return self.data.groupby('Month')['Sales'].sum().to_dict()

    def _identify_best_selling_product(self):
        total_sales = self.calculate_total_sales()
        return max(total_sales, key=total_sales.get)

    def _identify_month_with_highest_sales(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        return max(total_sales_per_month, key=total_sales_per_month.get)

    def analyze_sales_data(self):
        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()
        return {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales
        }

    def add_additional_data(self):
        total_sales = self.calculate_total_sales()
        minimest_selling_product = min(total_sales, key=total_sales.get)
        average_sales = sum(total_sales.values()) / len(total_sales)
        analysis_result = self.analyze_sales_data()
        analysis_result.update({
            'minimest_selling_product': minimest_selling_product,
            'average_sales': average_sales
        })
        return analysis_result


# =======================task3=======================
    def calculate_cumulative_sales(self):
         self.data['CumulativeSales'] = self.data.groupby('Product')['Sales'].cumsum()


    def add_90_percent_values_column(self):
        self.data['Discount90'] = self.data['Discount'] * 0.9


    def bar_chart_category_sum(self):
        sns.barplot(x='Product', y='Number of Selling',
                data=self.data.groupby('Product')['Number of Selling'].sum().reset_index())


    def calculate_mean_quantity(self):
        mean = np.mean(self.data['Total'])
        median = np.median(self.data['Total'])
        second_max = np.partition(self.data['Total'], -2)[-2]
        return mean, median, second_max


    def filter_by_sellings_or_and(self):
        filtered_data = self.data[((self.data['Number of Selling'] > 5) | (self.data['Number of Selling'] == 0))
                                  & ((self.data['Price'] > 300) & (self.data['Number of Selling'] < 2))]
        return filtered_data


    def divide_by_2(self):
        self.data['BlackFridayPrice'] = self.data['Price'] / 2


    def calculate_stats(self, columns=None):
        if columns is None:
            columns = self.data.columns
        stats = {}
        for col in columns:
            if np.issubdtype(self.data[col].dtype, np.number):  # Check if column contains numeric data
                stats[col] = {
                    'max': self.data[col].max(),
                    'sum': self.data[col].sum(),
                    'abs_sum': np.abs(self.data[col]).sum(),
                    'cum_max': self.data[col].cummax()
                }
        return stats

    # =============task 4=================


    def convert_date_format(self, date_columns: List = None):
        if date_columns is None:
            date_columns = ['Date']
        for col in date_columns:
            self.data[col] = pd.to_datetime(self.data[col])


    def categorize_prices(self):
        self.data['PriceCategory'] = pd.cut(self.data['Price'], bins=[0, 100, 200, 300, float('inf')],
                                            labels=['Low', 'Medium', 'High', 'Very High'], right=False)


    def change_index(self):
        self.data.set_index('CustomerId*Price', inplace=True)


    def split_and_concat(self):
        half = len(self.data) // 2
        df1, df2 = self.data.iloc[:half], self.data.iloc[half:]
        return pd.concat([df1, df2], axis=1)


    def complex_data_transformation(self):
        return self.data.T


    # def group_with_function(self, column_do, column_use, func):
    #     return self.data.groupby(column_do)[column_use].apply(func)
    def group_with_function(self, column_do, column_use, func):
        return self.data.groupby(column_do)[column_use].apply(func.__name__)

    # def locate_specific_row_by_index(self, index):
    #     return self.data.loc[index]
    def locate_specific_row_by_index(self, index):
        return self.data.iloc[index]

    def locate_specific_row_by_index_alternative(self, index):
        return self.data.iloc[index]


    def locate_specific_column_by_label(self, label):
        return self.data[label]


    def locate_specific_column_by_index(self, index):
        return self.data.iloc[:, index]


    def locate_specific_columns_and_rows(self, rows, cols):
        return self.data.iloc[rows, cols]


    def locate_specific_rows_and_columns(self, rows, cols):
        return self.data.iloc[rows, cols]


    def filter_by_mask(self, mask_list, is_by_index=False):
        if is_by_index:
            return self.data.loc[mask_list]
        else:
            return self.data[mask_list]
            # =============task 5=================
            # Task 26

    def handle_data_errors(self):
            try:
                # Check for missing files
                if self.data is None:
                    raise FileNotFoundError("No data provided.")

                # Check for missing columns
                required_columns = ['Product', 'Sales', 'Month', 'Number of Selling', 'Price', 'Discount', 'Total']
                missing_columns = [col for col in required_columns if col not in self.data.columns]
                if missing_columns:
                    raise ValueError(f"Missing columns: {missing_columns}")

            except Exception as e:
                print(f"Error: {e}")

            # Task 27

    def save_modified_sales_data(self):
            try:
                # Analyze the data
                analysis_result = self.analyze_sales_data()

                # Save analysis result to Excel file
                analysis_df = pd.DataFrame(analysis_result.items(), columns=['Metric', 'Value'])
                FileOperation().save_to_excel(analysis_df, "analyze_sales_data.xlsx")
                print("Analysis results saved successfully.")

            except Exception as e:
                print(f"Error occurred while saving analysis results: {e}")

            # Task 28

    @staticmethod
    def save_figures(path, figures):
            try:
                # Save figures to the specified path
                for i, fig in enumerate(figures):
                    fig.savefig(f"{path}/figure_{i + 1}.png")
                print("Figures saved successfully.")

            except Exception as e:
                print(f"Error occurred while saving figures: {e}")
