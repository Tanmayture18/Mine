class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class CircularLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            if node.next==self.head:
                break
            node=node.next  

    # Function for circular singly linkedlist
    def circular(self,nodevalue):
        newnode=Node(nodevalue)
        newnode.next=newnode
        self.head=newnode
        self.tail=newnode


cl=CircularLinkedlist()
cl.circular(4)


l1=[i.value for i in cl]
print(l1)


