import queue
class Queue:
    def __init__(self):
     self.q=queue.Queue()
     print("i have to loose weight:init")
    def put(self,item):
     self.q.put(item)
    def get(self):
     print("hello from the other side!:get")
     return self.q.get()

