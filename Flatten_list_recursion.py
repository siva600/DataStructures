
def flattern(l):
    output = []
    for item in l:
        if isinstance(item, list):
            flattern(l[item:])
        output.append(item)


l = [1 ,2 ,[3 ,4 ,[5 ,6 ,[7 ,8 ,[9 ,10]]]]]

print(flattern(l))





