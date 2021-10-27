# -*- coding: utf-8 -*-

import socket
from _thread import *
import time

HOST = "10.221.82.162"
#HOST = "192.168.0.40"
PORT = 25023

# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
client_socket.connect( (HOST, PORT) )
print("접속 성공")

# 수신 함수
def execute():
    while True:
        # 메시지를 수신합니다.
        print()
        data = client_socket.recv(1024)
        print("Received", repr(data.decode()) )

print("쓰레드 실행")
start_new_thread( execute, () )

print("입력 시작")
while True:
    # 메시지를 전송합니다.
    # print("입력해주세요: ", end="")
    client_socket.send( input().encode() )

# 소켓을 닫습니다.
client_socket.close()
