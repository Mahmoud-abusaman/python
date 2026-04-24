

class Node:

    def __init__(self, data,prev=None,next=None):

        self.data = data

        self.prev = prev

        self.next = next
 
 
class DoubleLinkedList:

    def __init__(self):

        self.head = None
 
 
#  Node0

    #  node1 node 2 node3   node 4

    def append_back(self, data):

        """Appends a new node with the given data to the end of the list.

        Parameters:

            data: The data to be stored in the new node.

        Returns:

            The updated DoubleLinkedList instance.

        """

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

            return self

        temp = self.head

        while temp.next != None:

            temp = temp.next

        temp.next = new_node

        new_node.prev = temp

        return self

 
    def append_front(self, data):

        newNode=Node(data)

        newNode.prev=None

        if self.head is None:

            self.head=newNode

            return self

        newNode.next=self.head

        self.head.prev=newNode

        self.head=newNode

        return self

    def _find_by_idx(self,idx):
        if(idx<0):
            raise IndexError("Index out of bounds")
        if(not self.head):
            raise IndexError("Index out of bounds")
        temp=self.head;
        while idx:
            temp=temp.next
            if(not temp):
                raise IndexError("Index out of bounds")
            idx-=1
        return temp
        


#   node0 node1 node2 node3 
    def delete_by_idx(self,idx):
        n=self._find_by_idx(idx)        
        if(not n.prev):
            if(not n.next):
                self.head=None
                return self
            self.head=n.next
            self.head.prev=None
            return self

        pre=n.prev
        nex=n.next
        pre.next=nex
        if(nex):
            nex.prev=pre
        return self

    def insert_by_idx(self,idx,val):
        if(idx<0):
            raise IndexError("Index out of bounds")
        if(not self.head):
            if(idx==0):
                self.head=Node(val)
                return self
            raise IndexError("Index out of bounds")
        if(idx==0):
            return self.append_front(val)

        prev=self._find_by_idx(idx-1)
        nex=prev.next

        added=Node(val,prev,nex)
        prev.next=added
        if(nex):
            nex.prev=added
        return self



    def display(self):

        """Displays the elements of the list in order."""

        current = self.head

        while current:

            print(current.data, end=' ')

            current = current.next

        print()

 
 
    def display_reverse(self):

        """Displays the elements of the list in reverse order."""

        current = self.head
        if(not current):
            print()
            return

        while current.next:

            current = current.next

        while current:

            print(current.data, end=' ')

            current = current.prev

        print()
 
