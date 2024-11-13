import pandas as pd
country_data = pd.ExcelFile('/.country_data_by_areaPopulation.xlsx', engine = 'openpyx1')
country_data
df1 = pd.read_excel(country_data, "Top 10 Population")
df1.head()

