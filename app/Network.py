import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.133.211"
        self.port = 5555
        self.addr = (self.server, self.port)


    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode("utf-8")
        except Exception as e:
            str(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)



