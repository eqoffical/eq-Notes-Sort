list = ["X", "A", "🚧", "C", "🚧 smth"]
print(list)

q_strings = []
other_strings = []

for s in list:
    if s[0] == "🚧":
        q_strings.append(s)
    else:
        other_strings.append(s)

output = q_strings + other_strings
print(output)
