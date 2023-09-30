class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def add_to_list(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    
    def print_nodes(self):
        curr = self.head
        while curr:
            print(curr.val, end = '-->')
            curr = curr.next
        print("")

    def add_head(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def count_nodes(self):
        pass

    def middle_node(self):
        pass

    def reverse_node(self):
        pass

    def remove_duplicate(self):
        pass
    




l = LinkList()
l.add_to_list(1)
l.add_to_list(2)
l.add_to_list(3)
l.print_nodes()