
"""
scraping => collecting
web scraping => scrape data from website and store them in a neceesary format
To create virtual environment=> python -m venv name => python -m venv example
To activate the environment => .\n<name>\Scripts\activate
To deactivate the environment => deactivate
how to share the list of packages with other developers
 -> requirements.txt   => this contains the output of pip list or pip freeze
    pip freeze. >requirements.txt
 -> how to install packages rom requirements.txt
    pip install -r requirements.txt
    r=>recursive(one after other packages installation)
"""

from bs4 import BeautifulSoup
import requests

r=requests.get("https://books.toscrape.com/")
#print(r.status_code)
content=r.content
print(type(content))
# print(content)
soup=BeautifulSoup(content,"html.parser")
print(type(soup))
soup=str(soup)
print(type(soup))
with open("scraping.html",'w') as fo:
    fo.write(soup)