import socket
import time

# Use urllib so that it counts the number of characters received and stops after 3000
# and displays total count at the end

url = input('Enter web server and page to request file from: ')
HOST = url.split('/')[0]
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = ('GET http://' + url + ' HTTP/1.0\r\n\r\n').encode()
count = 0
file = b""

try:
    mysock.send(cmd)
except:
    print('Error requesting file, please verify url is entered in this format: web.server/webPage')

while True:
    data = mysock.recv(500)
    time.sleep(.25)
    if (count + len(data)) <= 3000:
        count = count + len(data)
        print(len(data), count)
    if len(data) < 1: break
    file = file + data

mysock.close()
print(file.decode()[:count])
print('\n')
print('Limit {}, File length {}  '.format(3000, len(file.decode()[:count])))
