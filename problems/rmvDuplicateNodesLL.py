class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        current1 = head
        while current1:
            data = current1.data
            current2 = current1.next
            while current2:
                if current2.data == data:
                    if current1 is None:
                        self.head = self.head.next
                    else:
                        current1.next = current2.next
                current2 = current2.next
            current1 = current1.next
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 