import requests
import pandas as pd

url = 'https://github.com/danoc93/ista-2022-junio-python/blob/main/proyecto/'
html = requests.get(url).content
df_list = pd.read_html(html)

df = df_list[-1]
print(df)
df.to_csv('output.csv')