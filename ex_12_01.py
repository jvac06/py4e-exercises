import socket

#Use prompt so that user can enter any webpage they want to read, use error checking

url =input('Enter web server and page to request file from: ')
HOST = url.split('/')[0]
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = ('GET http://' + url + ' HTTP/1.0\r\n\r\n').encode()
try:
    mysock.send(cmd)
except:
    print('Error requesting file, please verify url is entered in this format: web.server/webPage')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
