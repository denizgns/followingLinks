import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#open url
url = 'http://py4e-data.dr-chuck.net/known_by_Kaelah.html'
html = urllib.request.urlopen(url).read()
#go through the 18th link for 7 times
for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    #finds the link
    tags = soup('a')
    print(tags[17])
    url = tags[17].get('href', None)
