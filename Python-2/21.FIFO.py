class QueueError(IndexError): # Eligir la clase base para la nueva excepción.
    pass

class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.insert(0, elem)

    def get(self):
        elem = self.__stk[-1]
        self.__stk.pop(-1)
        return elem

que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue Error")