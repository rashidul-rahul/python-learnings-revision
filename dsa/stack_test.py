class Stack:
    def __init__(self):
        self.item_list = []

    def push(self, data):
        self.item_list.append(data)

    def pop(self):
        if self.is_empty():
            return "list is empty"

        return self.item_list.pop()

    def is_empty(self):
        if self.item_list == []:
            return True

        return False


if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(2)
    stack1.push(3)
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())