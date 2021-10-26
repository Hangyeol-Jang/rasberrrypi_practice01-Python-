# -*- coding: utf-8 -*-
import threading
from _thread import *
import time

def execute1():
	while True:
		print("실행1")
		time.sleep(1)
		
def execute2(num):
	while True:
		print("실행2")
		time.sleep(1)
		
def threaded(msg):
	while True:
		print(msg)
		time.sleep(1)
		
# execute()
thread_ex = threading.Thread( target=execute2, args=(5,) )
thread_ex.start()

thread_ex1 = threading.Thread(target=execute1, args=() )
thread_ex1.start()

start_new_thread(threaded, ("output",) )

print("실행3")
