# -*- coding: utf-8 -*-
from datetime import datetime as day
import socket
HOST = "192.168.0.40"
PORT = 25023

# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결을 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind( (HOST, PORT) )
# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()
# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소입니다.
print("Connected by", addr)

data = client_socket.recv(1024)
print("Received from", addr, data.decode() )
msg = "{0} {1}".format(day.now(), data.decode())
client_socket.send(msg.encode() )

client_socket.close()
server_socket.close()
