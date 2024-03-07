"""
Python Extract Transform Load Example
"""

import requests
import pandas
import sqlite3 

url='https://api.coincap.io/v2/assets'
header={"Content-Type":"application/json","Accept-Enconding":"deflate"}

response = requests.get(url, headers=header)
#print(response)
responseData = response.json()
#print(responseData)

df = pandas.json_normalize(responseData,'data')
#print(df)

connection = sqlite3.connect('mydata.db')
df.to_sql(name = 'MyCriptoData', con = connection, index = False, if_exists = 'fail')