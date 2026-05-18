class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
 
 
class SList:
    def __init__(self):
        self.head = None
 
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
 
    def add_to_back(self, val):
        new_node = SLNode(val)
        
        if self.head is None:
            self.add_to_front(val)
        else:
            runner = self.head
            while runner.next is not None:
                runner = runner.next
            runner.next = new_node
        return self
 
    def print_values(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return self
 
    def remove_from_front(self):
        if self.head is None:
            return None
        
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value
 
    def remove_from_back(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        
        removed_value = runner.next.value
        runner.next = None
        return removed_value
 
    def remove_val(self, val):

        if self.head is not None and self.head.value == val:
            self.head = self.head.next
            return
        
        runner = self.head
        while runner is not None and runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return
            runner = runner.next
 
