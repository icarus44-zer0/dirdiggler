import pandas as pd 
import requests
from bs4 import BeautifulSoup

def get_body(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,features="html.parser")
    return soup.get_text()


for i in range (100): 
	base = 'http://10.10.27.42/note.php?note='
	inc = str(i)
	url = base + inc
	ret = get_body(url)

	if ret:
		print(ret.strip())