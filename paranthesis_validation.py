from stack import Stack


def par_validation(string):
    s1 = Stack()
    s2 = []
    for item in range(0, len(string)//2):
        s1.push(string[item])
    for item in range(len(string)//2, len(string)):
        s2.append(string[item])
    s2 = s2[::-1]
    print(s1.get_stack())
    print(s2)
    hashing = {"(": ")", "{": "}", "[": "]"}
    balanced = True

    if len(string) % 2 != 0:
        return "not balanced, no of item count not matching"
    else:
        while len(s2) != 0 and balanced:
            s1_popped_item = s1.pop()
            s2_popped_item = s2.pop()
            if hashing[s1_popped_item] == s2_popped_item:
                balanced = True
            else:
                balanced = False

    return balanced

# print(par_validation("{[({)]}}"))
# print(par_validation("[((([()])))}"))
print(par_validation("[]()()(((([])))"))
