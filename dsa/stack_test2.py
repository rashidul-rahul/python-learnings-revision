forward = []
backward = []


def stack_test(action, url=None):
    if action == "new":
        backward.append(url)
        return url

    if action == "next":
        if forward == []:
            return False

        url = forward.pop()
        backward.append(url)
        return url

    if action == "back":
        if backward == []:
            return False
        url = backward.pop()
        forward.append(url)
        return url


stack_test("new", "asdf")
stack_test("new", "erdsr")
stack_test("new", "ttewcxr")

print(stack_test("back"))
print(stack_test("back"))
print(stack_test("next"))
print(stack_test("next"))
