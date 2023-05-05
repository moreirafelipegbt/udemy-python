#Daemon threads are terminated if all other normal threads finish execution
#But the Python process is not terminated if at least 1 noemal thread is running

import threading

def normal_operation():
    while True:
        print('Normal thread is running...')

def daemon_operation():
    while True:
        print('Daemon thread is running...')

t1 = threading.Thread(target=normal_operation, name="Normal Thread #1")
t2 = threading.Thread(target=daemon_operation, name="Normal Thread #2")
t1.start()
t2.start()