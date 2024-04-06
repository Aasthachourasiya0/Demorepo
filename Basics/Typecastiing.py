# float to integers
# x = 3.14
# y = int(x)
# print(y) #3

# int to float
# x = 15
# y = float(x)
# print(y) #15.0

# str
# x = "Astha"
# y = list(x)
# print(y)  #['A', 's', 't', 'h', 'a']

# str to intergers
# x = "abc"
# try: 
#     y = int(x)
#     print("Converted Integer:" , y)
# except ValueError:
#     print("invalid interger represent in the string.")


# boolean gives True False output
# x = 1
# y = 5
# print(x>y) #False
# print(x==y) #Fasle
# print(x<y) #True


#tuple 
# x = [1, 2, 3, 4, 6]
# y = tuple(x)
# print(y) #(1, 2, 3, 4, 6)

# set {1, 2, 3, 4}
x = {1, 2, 3, 4}
y = {4, 5, 6, 5}
print(x.union(y)) #{1, 2, 3, 4, 5, 6}
print(x.intersection(y)) #{4}
print(y.difference(x))  #{5, 6}

