# Retrieve tag at specific location by following links a specific amount of times

import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# input values
f_url = input('Enter Url: ')
repeat = int(input('# of Repeats: '))
index = int(input('position of tag(#): ')) - 1

# ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# retrieve links
url = f_url
for i in range(repeat):
     html = urlopen(url, context=ctx).read()
     soup = BeautifulSoup(html, 'html.parser')
     links = [tag.get('href', None) for tag in soup('a')]
     print('Retreiving:', links[index])
     url = links[index]