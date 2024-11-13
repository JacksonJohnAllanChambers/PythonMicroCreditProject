import pandas as pd
country_data = pd.ExcelFile('./country_data_by_areaPopulation.xlsx', engine = 'openpyxl')
country_data

df1 = pd.read_excel(country_data, "Top 10 Population")
df1.head()
df2 = pd.read_excel(country_data, "Top 10 Total Area")
df2.head()
frame = [df1,df2]
country_data1 = pd.concat(frame)
country_data1
#pd.merge
top_countries = pd.merge(df1,df2,on=['Country'],how="outer")
top_countries['Country'] == 'India'
top_countries[top_countries['Country'] == 'India']
#check pop of india
top_countries[top_countries['Country'] == 'India']['Population_x']
