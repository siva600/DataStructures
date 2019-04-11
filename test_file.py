def dict_items(letter_values):
    x = {}
    for key, value in letter_values.items():
        if value in x.keys():
            x[value].append(key)
        else:
            x[value] = [key]
    return x


letter_values = {"output.txt": "sam", "java.txt": "siva", "python.txt": "jam", "Oracle.txt": "siva"}


def find(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start+end)//2
        if target == L[middle]:
            return True
        elif target > L[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False


def max(data):
    values = list(data.values())
    maximm = values[0]
    for item in values:
        if item > maximm:
            maximm = item

    return maximm


def most_repeated_word(file):
    data = {}
    best_word = 0
    with open("check_check.txt", 'r') as f:
        x = [word.lower() for line in f for word in line.split() if len(word) == 4]
        for item in x:
            if item in data.keys():
                data[item] += 1
            else:
                data[item] = 1
    for key, value in data.items():
        if value == max(data):
            best_word = key
    print(x)
    return "Most repeated item, {} : {}".format(best_word, max(data))

print(most_repeated_word("file.txt"))


