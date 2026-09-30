
import socket
import threading

HOST = '10.4.1.114'                
PORT = 5003     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def connection (conn, addr): 
    print ('Connected by',addr)
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
        print(data)
    conn.close()
# liste de client qu'il manqque avec une boucle pour ne plus renvoyer au client son propre messagge mais plutot le mesage a qu'il a dit 
# et je crois aussi envoyer une list au client pour voir les client dispo et leur envoyer le message

while True :

    conn, addr = s.accept()
    thread_1 = threading.Thread(target= connection, args=(conn, addr))
    thread_1.start()



