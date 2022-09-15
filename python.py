from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas_profiling import ProfileReport
url = "https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid"
page = requests.get(url)
htmlContent = page.text
soup = BeautifulSoup(htmlContent, 'html.parser')
table = soup.find('table', class_="table")
heard = []
for i in table.find_all('th'):
    title = i.text
    title = i.text.strip()
    heard.append(title)
df = pd.DataFrame(columns=heard)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    lenght = len(df)
    df.loc[lenght] = row_data
df.to_csv('data/web srapped data.csv')
df = pd.read_csv('data/web srapped data.csv')
profile = ProfileReport(df)
profile.to_file(output_file="data/web.html")