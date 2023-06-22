from threading import Thread

class MyThread(Thread):

    def __init__(self, name="My Thread", count=100):
        Thread.__init__(self, name=name)
        self.count = count

    def run(self):
        for i in range(self.count):
            print(f'{self.getName()}: {i}')

task1 = MyThread()
task1.start()
task2 = MyThread("Another Thread", 100)
task2.start()