import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find the target table
table = soup.find("table", {"id": "constituents"})
if table is None:
    raise Exception("Table not found")

# Convert HTML table to DataFrame
df = pd.read_html(str(table))[0]

# Keep only useful columns
df = df[["Symbol", "Security", "GICS Sector", "Date added"]]
df.rename(columns={"Security": "Company_Name", "GICS Sector": "Sector"}, inplace=True)

# Save to Excel
df.to_excel("SP500_Scraped_Data.xlsx", index=False)

print(df.head())
print("Saved to SP500_Scraped_Data.xlsx")