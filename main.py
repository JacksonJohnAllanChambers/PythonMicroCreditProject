import pandas as pd
#df1 = CityList.csv
#df2 = table 1 - CityList-2.xlsx
#df3 = table 2 - CityList-2.xlsx
#need to ensure all data columns match
#-----/////Make pandas files df1, df2, df3////----
CL2 = pd.ExcelFile('./CityList-2.xlsx', engine = 'openpyxl')
df1 = pd.read_csv('./CityList.csv')
df2 = pd.read_excel(CL2, "Page1")
df3 = pd.read_excel(CL2, "Page2")
#------///// Make data all same shape////---

df2[['Name','CountryCode','Population']] = df2['Name;CountryCode;Population'].str.split(";",expand=True)
del df2['Name;CountryCode;Population']
df1['Population'] = df1['Population'].astype(int)
df2['Population'] = df2['Population'].astype(int)
df3['Population'] = df3['Population'].astype(int)
#df2.head()
#----/// First Merge///----
df12 = pd.merge(df1,df2,on=['Name','Population','CountryCode'],how="outer")
#----///Second merge///----
df123 = pd.merge(df12,df3,on=['Name','Population','CountryCode'],how="outer")
df123.drop(df123.columns[df123.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df123.head(100)
# print(df123)
df123.to_csv('out.csv', index=False)
#-----////Find Total World Pop///------
print("The Biggest City in the World is\n",df123.loc[df123["Population"].idxmax()])
#-----////Find city in brazil with biggest population////---
Brazil =df123[df123['CountryCode'] == 'BRA']
Brazil_Pop =Brazil.loc[Brazil['Population'].idxmax()]
print("Biggest City in Brazil is\n",Brazil_Pop)
Brazil_total_pop = Brazil['Population'].sum()
print("The Total Population of Brazil is",Brazil_total_pop)
#----///Find the populations in canada of Burnaby, Coquitlam, and Delta///----
Canada =df123[df123['CountryCode'] == 'CAN']
Burnaby_pop = Canada[Canada['Name']== "Burnaby"]
print(Burnaby_pop)
Coquitlam_pop = Canada[Canada['Name']== "Coquitlam"]
print(Coquitlam_pop)
Delta_pop = Canada[Canada['Name']== "Delta"]
print(Delta_pop)
total_select_CAN_CITY = Burnaby_pop["Population"].sum() + Coquitlam_pop["Population"].sum() + Delta_pop["Population"].sum()
print("The total pop in these Three select canadian citys is",total_select_CAN_CITY)