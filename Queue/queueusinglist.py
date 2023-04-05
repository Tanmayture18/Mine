class Queue:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=[str(x) for x in self.list]
        return " ".join(values)

    def is_empty(self):         # O(1)
        if self.list==[]:
            return True
        else:
            return False
        
    def enqueue(self,value):    #O(1) 
        self.list.append(value)

    def dequeue(self):         # O(1)
        if self.is_empty():
            return "Empty"
        else:
            return self.list.pop(0)

    def peek(self):       # O(1)
        if self.is_empty():
            return 'Empty'
        else:
            return self.list[0]

    def delete(self):  #O(1)
        self.list=None  


queue=Queue()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.peek())
queue.delete()
print(queue)
               
            