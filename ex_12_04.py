# extract and count paragraph <p> tags and display the count of the paragraphs as output of your program.
# test on multiple sites


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# create context to ignore
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get Url and save it into BeautifulSoup handle
url = input('Enter Url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all paragraphs and count them
paras = soup('p')
print(len(paras))
