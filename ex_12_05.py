import socket
import time
#Change socket so that it does not display header or newline after the header

url =input('Enter web server and page to request file from: ')
HOST = url.split('/')[0]
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = ('GET http://' + url + ' HTTP/1.0\r\n\r\n').encode()
content = b""

try:
    mysock.send(cmd)
except:
    print('Error requesting file, please verify url is entered in this format: web.server/webPage')

while True:
    data = mysock.recv(512)
    time.sleep(0.25)
    if len(data) < 1:
        break
    content = content + data

mysock.close()

# Find position of header
pos = content.find(b'\r\n\r\n')

# Print only content, 4 bits after so it won't show new line
print(content[pos+4:].decode())