import asyncio
import time
import threading

jugador = 0

def asyncrona ():
    for j in range(1,10):
        global jugador
        jugador = j
        #print (f"dentro:{j}")
        time.sleep(1)
    

def user_input():
    while True:
        m = input()
        if m == 'q': break
        print (f"fuera:{jugador}")


t1 = threading.Thread(target=asyncrona)
t1.start()


user_input()