﻿import threading,multiprocessing

def loop():
	x=0
	while True:
		x=x^1
		
for i in range(multiprocessing.cup_count()):
	t=threading.Thread(target=loop)
	t.start()