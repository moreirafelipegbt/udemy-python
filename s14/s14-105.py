import threading

def count_operation():
    for i in range(100):
        print(threading.current_thread().name + str(i))


t1 = threading.Thread(target=count_operation, name='Thread #1')
t2 = threading.Thread(target=count_operation, name='Thread #2')

t1.start()
t2.start()

t1.join()
t2.join()