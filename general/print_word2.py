a = "word3"
space = ""

for i in a:
    space += " "

print(f"+{a}+")
for i in a:
    print(f"{i}{space}{i}")
print(f"+{a}+")


a = "word3"
space = ''
for i in a:
    print(f"{space}{i}")
    space += " "
