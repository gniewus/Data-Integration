import requests
import pandas as pd
import numpy as np
input_file = "inputDB.csv"
usa_file = "postcodes.csv"
output_file = "cleaned.csv"
data = pd.read_csv(input_file)
usa_data = pd.read_csv(usa_file,usecols=[0,1,3])

data.head()
data.shape
data.columns
df = pd.DataFrame(data=data)
df3 = pd.DataFrame(data=usa_data)
df2 = df.copy()
df_usa = df3.copy()

for col in data.columns:
    df2[col] = df2[col].str.upper()

df2.head()
df2.shape
df2["SSN"] = df2["SSN"].str.replace(r'[a-zA-Z .+!@#$%^&*-]+','')
df2.to_csv(output_file,sep=',',index=False)


df2["ZIP"] = df['ZIP'].str.replace(r'[a-zA-Z .+!@#$%^&*]+','')
df2.to_csv(output_file,sep=',',index=False)
df_usa = df_usa.rename(index=str, columns={"Zip Code": "ZIP"})
df2['ZIP'] = pd.to_numeric(df2['ZIP'])
df4 = df2.merge(df_usa, left_on='ZIP', right_on='ZIP', how='left')
df4 = df4.drop(['City','State'], 1)
df4 = df4.rename(index=str, columns={"Place Name": "City"})
df4 = df4.rename(index=str, columns={"State Abbreviation":"State"})

df4['City'] = df4['City'].str.upper()
df4 = df4[['RecID', 'FirstName', 'MiddleName', 'LastName', 'Address', 'City',
       'State', 'ZIP', 'POBox', 'POCityStateZip', 'SSN', 'DOB']]
df4.to_csv(output_file,sep=',',index=False)

