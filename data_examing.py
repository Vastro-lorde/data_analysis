import pandas as pd
import matplotlib.pyplot as plt
import datetime

melbourne_file_path = './data/melb_data.csv'
sales_file_path = './data/sales_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
sales_data = pd.read_csv(sales_file_path)

# print(melbourne_data.Suburb == 'Williamstown')
# print(melbourne_data.iloc[1])
# print(melbourne_data.loc[(melbourne_data['Price'] > 1000000)])
# print(melbourne_data.iloc[0:5, 0:5])
# print(melbourne_data.shape)
# print(melbourne_data["Price"].describe())
# print(melbourne_data.info())

# # Plot the density plot
# melbourne_data["Price"].corr().plot(kind='hist', figsize=(14, 6))
# plt.title('Density Plot of Melbourne House Prices')
# plt.ylabel('Density')
# plt.xlabel('Price')
# plt.show()

# numeric_cols = sales_data.select_dtypes(include=['number'])

# # Compute correlations
# correla = numeric_cols.corr()

# # Plot correlation matrix
# figure = plt.figure(figsize=(14, 6))
# plt.matshow(correla, fignum=figure.number, cmap='RdBu')
# plt.xticks(range(len(correla.columns)), correla.columns, rotation=90)
# plt.yticks(range(len(correla.columns)), correla.columns)
# plt.colorbar(label='Correlation')
# plt.title('Correlation Matrix')
# plt.show()

# print( melbourne_data["Price"].mean() )
# print( melbourne_data["Price"].std() )
# print(datetime.datetime.now().year - melbourne_data["YearBuilt"].max())
# melbourne_data_display = melbourne_data.describe()
# print( melbourne_data_display )

# print(melbourne_data.columns)

# new_data = pd.DataFrame({ "x": [1, 2, 3], "y": [4, 5, 6], "z": [7, 8, 9] }, index=["a", "b", "c"])

# print(new_data.iloc[:, 2])
# print(new_data)

# print("a median: ",new_data.loc["a"].median())



# primeList = [ i for i in range(100) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
# primeList = [1,2,5] + primeList
# print(primeList)
# print("even list: ",pd.Series(primeList, dtype="int", name="prime"))
# print("even median: ",pd.Series(primeList).median())