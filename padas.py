import requests
from bs4 import BeautifulSoup
import pandas as pd 

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/')
for df in dfs:
	print(df)