class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_data_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def insert_data_at_ending(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def delete_data(self, key):
        tmp = self.head

        if tmp and tmp.data == key:
            self.head = tmp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if not temp:
            print("key not found")
        
        prev.next = temp.next
        temp = None

    def display(self):
        if not self.head:
            print("no data in list")
            return
        tmp = self.head
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next
        print("end")


ll = LinkedList()
ll.insert_data_beginning(4)
ll.insert_data_at_ending(5)
ll.insert_data_beginning(6)
ll.display()
