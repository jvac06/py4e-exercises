# Count & Sum Number of comments in JSON

import ssl
import json
import urllib.request, urllib.error

# Ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Import data using JSON
url = input('Enter Url: ')

print('Retreiving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Convert to JSON
js = json.loads(data)

# Iterate and save counts as int
nums = []
for cmt in js['comments']:
    nums.append(cmt['count'])

# Print Solution
print('Count:', len(nums))
print('Sum:', sum(nums))
