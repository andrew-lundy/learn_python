# Exercise: https://www.learnpython.org/en/Pandas_Basics

import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

house_rent_prices = pd.read_csv('House_Rent_Dataset.csv', index_col=0)
print(house_rent_prices)
print(house_rent_prices[['Rent', 'Area Locality']])
print(house_rent_prices[0:4])