class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []

        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)

    def append(self, data):
        node = Node(data=data)
        if self.head.next == None:
            self.head.next = node
            return

        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node

    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(prev=None, next=first_node, data=data)

        self.head.next = new_node
        if first_node:
            first_node.prev = new_node

    def search(self, search_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == search_data:
                return current_node

            current_node = current_node.next

        return None

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next

        if node.next:
            node.next.prev = node.prev

    def remove(self, data):
        node = self.search(data)
        if node is None:
            return

        self.remove_node(node)


ll = DoublyLinkedList()

ll.append(3)
ll.append(4)
ll.prepend(12)
ll.remove(3)
ll.prepend(2)

print(repr(ll))
