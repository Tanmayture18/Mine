class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next     

    # Traversing Linked List     O(N)
    def traverse(self):

        # Empty Linkedlist
        if self.head is None:
            print("Empty LinkedList")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next

    # Searching   O(N)
    def search(self,nodevalue):
        if self.head is None:
            return "Empty LinkedLIst"
        else:
            node=self.head
            while node is not None:
                if node.value==nodevalue:
                    return node.value
                node=node.next
            return 'element does not exists'        


    def insert(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head= newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode


l=LinkedList()
l.insert('Tans',0) 
l.insert('Ture',1)  
l.insert('Tanmay',0) 
l.insert('ture',0)
l.insert('TURE',2)
print([node.value for node in l]) 
l.traverse()

print("___________________________")

print(l.search('Tanmay'))
print(l.search('Dipak'))
