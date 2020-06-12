import urllib.request
import time

# Use urllib so that it counts the number of characters received and stops after 3000
# and displays total count at the end

url = input('Enter web server and page to request file from: ')
count = 0
file = []

try:
    fhand = urllib.request.urlopen('http://' + url)
except:
    print('Error requesting file, please verify url is entered in this format: web.server/webPage')

for line in fhand:
    chars = list(line.deconde())
    file = file.append(chars)
    while count <= 3000:
        count = count + len(chars)
        print(len(chars), count)
print("".join(chars))
print('\n')
print('Limit {}, File length {}  '.format(3000, len(chars[:count])))
# while True:
#     data = mysock.recv(500)
#     time.sleep(.25)
#     if (count + len(data)) <= 3000:
#         count = count + len(data)
#         print(len(data), count)
#     if len(data) < 1: break
#     file = file + data
#
# mysock.close()
# print(file.decode()[:count])

