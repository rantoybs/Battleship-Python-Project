import socket
from requests import get

import time


class Network:

    def __init__(self, ip_address=None):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(60)

        self.server = ip_address
        if self.server is None:

            self.server = socket.gethostbyname_ex(socket.gethostname())[-1]
            for i in self.server:
                if i[0]+i[1]+i[2] == '127':     # Checks to see whether IP is a loopback address
                    continue
                elif i[0]+i[1]+i[2] == '192':
                    self.server = i
                elif i[0] + i[1] != '10':
                    self.server = i
                else:
                    self.server = i
                    break
        print(self.server)

        self.port = 5555
        self.addr = (self.server, self.port)
        self.client.connect(self.addr)
        self.p = self.client.recv(2048).decode()



    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data.encode())
            time.sleep(1)

        except socket.error as e:
            print(e)

    def receive(self):

        try:
            msg = self.client.recv(2048).decode()
            return msg

        except socket.error as e:
            print(e)

    def getIP(self):
        return self.server[-1]
