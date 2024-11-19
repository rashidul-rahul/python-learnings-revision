class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __find_nodes(self, data=None):
        """will use it later"""
        current_node = self.head.next
        while current_node.next:
            if data and current_node.data == data:
                return current_node
            current_node = current_node.next

        if data and current_node.data != data:  # if there is data and not return the value it means node not found in the linked list
            return None
        else:
            return current_node

    def append(self, data):
        """
        It can add an item after the last node
        """
        new_node = Node(data=data)
        if not self.head.next:
            self.head.next = new_node
            return
        # last_node = self.__find_nodes()  # No data added because we need the last node
        # last_node.next = new_node
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data):
        """
        It can add before the first item
        """
        new_node = Node(data)
        self.head.next, new_node.next = new_node, self.head.next

    def insert(self, data, new_data):
        """
        It will insert after a specific node
        """
        # specific_node = self.__find_nodes(data)
        # if specific_node:
        #     new_node = Node(new_data)
        #     specific_node.next, new_node.next = new_node, specific_node.next
        #     return

        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                new_node = Node(new_data)
                current_node.next, new_node.next = new_node, current_node.next
                return

            current_node = current_node.next

        print("Node is not matching...")

    def search(self, data):
        """
        It can search a specific node. If there is same node more than one time
        it can only find the first one.
        """
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                print("Data found:", current_node.data)
                return

            current_node = current_node.next

        print("Node is not matching...")

    def remove(self, data):
        """
        It can remove a specific node from the list. If the same node
        twice in that list it will only remove the first one find
        """
        temp_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                temp_node.next = current_node.next
                return
            temp_node = current_node
            current_node = current_node.next

        print("Node is not matching...")

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return "=>".join(nodes)


ll = LinkedList()
ll.append(2)
ll.append(3)
ll.prepend(5)
ll.prepend(9)
ll.insert(2, 10)
ll.insert(3, 29)
ll.search(3)

print(ll)
ll.remove(7)
print(ll)
