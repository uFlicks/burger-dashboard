import requests
import duckdb
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
# Access variables
api_key = os.getenv("API_KEY")
db_name = os.getenv("DB_NAME")


url = "https://burgers-hub.p.rapidapi.com/burgers"

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "burgers-hub.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
res = response.json()

burger_data = {
    "id": [i['id'] for i in res],
    "name": [i['name'] for i in res],
    "price": [i['price'] for i in res],
    "veg": [i['veg'] for i in res]
}
df = pd.DataFrame(burger_data)


con = duckdb.connect(f"{db_name}.duckdb")
result = con.execute("""
    SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_name = 'burgers'
""").fetchone()

if result[0] == 0:
    # Table doesn't exist; create it
    con.from_df(df).create("burgers")
else:
    print("Table 'burgers' already exists. Skipping creation.")



