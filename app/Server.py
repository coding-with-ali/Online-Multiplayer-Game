from _thread import *
import socket

global currentPlayer
currentPlayer=0
server = socket.gethostbyname(socket.gethostname())
port = 5555
print(f"The server is running on ip {server} and port {port}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("waiting for connections, Server started")

turn=True
clients_info = [(0,20,turn), (0,20,turn)]


def threaded_client(conn, player):
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            clients_info[player] = data
            if not data:
                print("Disconnected")
                global currentPlayer
                currentPlayer-=1
                break
            else:
                if player == 1:
                    reply = clients_info[0]
                else:
                    reply = clients_info[1]



                print("Received:", data)
                print("sending :", reply)
                print("total Players:", player)

            conn.sendall(str.encode(str(reply)))
        except:
            break

    print("lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print("total players :"+ str(currentPlayer))
