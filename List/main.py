num = [1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]

for number in num:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)

print("Even number :",even)
print("odd number :",odd)


num = [1,2,3,4,5,6,7,8,9,10]
reverse_num = []

for i in range(len(num)-1,-1,-1):
    reverse_num.append(num[-1])

print(reverse_num)


# #slicing
num = [1,2,3,4,5,6,7,8,9,10]
print(num[::-1])

#LIST Comphrenhension
num = [1,2,3,4,5,6,7,8,9,10]
even=[x for x in num if x%2!=0]
print(even)

num = [1,2,3,4,5,6,7,8,9,10]
even=[i for i in num if i%2==0]
print(even)