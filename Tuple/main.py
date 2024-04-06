num = (1,2,3,4,5,2)

print(id(num))
x = list(num)
x.append(34)
num = tuple(x)

print(id(num))