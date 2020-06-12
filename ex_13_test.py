# Retrieve the sum of comment counts from XML in url

import ssl
import xml.etree.ElementTree as ET
from urllib.request import urlopen

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# fetch XML from url
url = input('Enter Url: ')
xml = urlopen(url, context=ctx)
tree = ET.fromstring(xml.read())

# iterate & save count as int
counts = tree.findall('.//count')
numbers = []
for count in counts:
    numbers.append(int(count.text))

# print solution
print('Counts:', len(numbers))
print('Sum:', sum(numbers))