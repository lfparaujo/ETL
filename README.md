# ETL


<span style="font-size: larger;"> Python Extract Transform Load Example Explanation </span>

This Python script is an example of an Extract, Transform, Load (ETL) process using data from a cryptocurrency API. The ETL process involves extracting data from an API, transforming it into a suitable format, and loading it into a SQLite database.

<span style="font-size: larger;">Step 1: Extracting Data from a Cryptocurrency API </span>

________________________
url = 'https://api.coincap.io/v2/assets' 

header = {"Content-Type": "application/json", "Accept-Encoding": "deflate"}

response = requests.get(url, headers=header)
________________________

The script uses the requests library to send an HTTP GET request to the specified cryptocurrency API (https://api.coincap.io/v2/assets).
The header variable contains information about the request, specifying the content type and encoding.


<span style="font-size: larger;">Step 2: Handling the API Response </span>

________________________
responseData = response.json()
________________________


The API response is in JSON format, and response.json() is used to convert it into a Python dictionary.
The resulting data is stored in the responseData variable.


<span style="font-size: larger;"> Step 3: Transforming Data with Pandas </span>

________________________
df = pandas.json_normalize(responseData, 'data')
________________________

The pandas library is employed to transform the nested JSON data into a structured DataFrame.
The json_normalize function is applied to flatten the nested structure of the 'data' field in the JSON, creating a DataFrame (df).


<span style="font-size: larger;"> Step 4: Creating a SQLite Connection and Loading Data </span>

________________________
connection = sqlite3.connect('mydata.db')
df.to_sql(name='MyCryptoData', con=connection, index=False, if_exists='fail')
________________________

A connection to a SQLite database (mydata.db) is established using sqlite3.connect().
The DataFrame df is loaded into the SQLite database using the to_sql method from Pandas.
The table is named 'MyCryptoData' in the SQLite database.
The if_exists='fail' parameter ensures that if the table already exists, the script will not overwrite it.


In summary, this Python script extracts cryptocurrency data from an API, transforms it into a structured format using Pandas, and then loads it into a SQLite database. This process is a fundamental example of the ETL paradigm commonly used in data engineering and analysis.
