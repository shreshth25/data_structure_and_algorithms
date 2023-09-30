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
        c = 0
        curr = self.head
        while curr:
            curr = curr.next
            c+=1
        print(f"No. of nodes are {c}")

    def middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle element is {slow.val}")

    def reverse_node(self):
        pass


    def remove_duplicate(self):
        pass
    




l = LinkList()
l.add_to_list(1)
l.add_to_list(2)
l.add_to_list(3)
l.add_to_list(4)
l.add_to_list(5)
l.add_head(0)
l.print_nodes()
l.count_nodes()
l.middle_node()