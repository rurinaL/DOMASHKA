import requests
from bs4 import BeautifulSoup
import json
url = 'https://panorama.pub'
csport_request=requests.get(url)
csport_content=csport_request.text
parsed_page=BeautifulSoup(csport_content)
lul=parsed_page.find_all('h3','a')
itog = json.dumps(lul)
print(itog)