from threading import Thread

class Counter(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def couting_threads(self):
        for i in range(100):
            print('%s thread is runing: %s' % (self.name, str(i)))

t1 = Counter('Thread 1')
t2 = Counter('Thread 2')

t1.start()
t2.start()

t1.couting_threads()
t2.couting_threads()