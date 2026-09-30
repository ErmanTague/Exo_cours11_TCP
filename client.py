

import socket

HOST = '10.4.1.110'
PORT = 5003    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'bonjour')
data = s.recv(1024)
s.close()
print ('Received', repr(data))