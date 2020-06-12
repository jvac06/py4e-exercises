# Fetch span tags content(numerical) and add them

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# fetch & organize data in bs4
url = input('Enter Url: ')
html = urllib.request.urlopen(url, context=ctx)
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')

# loop through tags & add to list
content = list()
for span in spans:
    content.append(int(span.contents[0]))

print('Count', len(content))
print('Sum', sum(content))