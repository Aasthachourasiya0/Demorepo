

# num = int(input("Enter the num : ")) #16434
# digit = 0
# t1 = num
# while(t1>0) : 
#     digit+=1
#     t1//=10 #0

# t2 = num
# sum = 0 #16434
# while(t2>0) : #0
#     rem = t2%10 #1
#     multi = 1 #1
#     for i in range(1,digit+1):
#         multi*=rem
#     sum+=multi
    
#     t2//=10 #0

# if(num==sum) :
#     print(num, "is A number")
# else:
#     print(num, "is not A number")




# acount = 0
# asum = 0
# aproduct = 1
# for j in range(100, 10000) :
#     num = j
#     digit = 0
#     t1 = num
#     while(t1>0) :
#         digit+=1
#         t1//=10
# t2 = num
# sum = 0
# while(t2>0) :
#     rem = t2%10
#     multi = 1
#     for i in range(1,digit+1):
#         multi*=rem
#     sum+=multi
#     t2//=10
# if (num==sum) :
#     print(num)
#     acount+=1
#     asum+=num
#     aproduct*=num


num = 1634
num = int(input("Enter the num : "))
digit = 0
t1 = num
while(t1>0) : 
    digit+=1
    t1//=10 

t2 = num
sum = 0 
while(t2>0) : 
    rem = t2%10 
    multi = 1 
    for i in range(1,digit+1):
        multi*=rem
    sum+=multi
    
    t2//=10 

if(num==sum) :
    print(num, "is A number")
else:
    print(num, "is not A number")