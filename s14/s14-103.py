import threading

def count_operation():
    for i in range(100):
        print(threading.current_thread().name + str(i))

#count_operation()
#count_operation()

t1 = threading.Thread(target=count_operation, name='Adam')
t2 = threading.Thread(target=count_operation, name='Joe')

t1.start()
t2.start()