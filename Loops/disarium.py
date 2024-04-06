# # find number of digits
# for j in range(10,10000): 
#     num = j
#     t1 = num #1634

#     digits = 0  #4
#     while(t1>0): #0
#         digits+=1
#         t1//=10

#     t2 = num
#     sum = 0
#     while(t2>0):
#         rem = t2%10
#         multi = 1
#         for i in range(digits,0,-1):
#             multi*=rem
#         digits-=1
#         sum+=multi
#         t2//=10

#     if num==sum:
#         print(num,"is an disarium number")





#check 175 is disarm nu
# num = 175
# num = int(input("Enter the num : "))
# digit = 0
# t1 = num
# while(t1>0) : 
#     digit+=1
#     t1//=10 

# t2 = num
# sum = 0 
# while(t2>0) : 
#     rem = t2%10 
#     multi = 1 
#     for i in range(1,digit+1):
#         multi*=rem
#     sum+=multi
    
#     t2//=10 

# if(num==sum) :
#     print(num, "is disarim number")
# else:
#     print(num, "is not disarium number")


#print all disarium num between 1 to 100
for j in range(1,101):
    num = j
    t1 = num

    digits = 0
    while(t1>0):
        digits+=1
        t1//=10

    t2 = num
    sum = 0
    while(t2>0):
        rem = t2%10
        multi = 1
        for i in range(digits,0,-1):
            multi*=rem
        digits-=1
        sum+=multi
        t2//=10

    if num==sum:
        print(num,"is an disarium number")
else:
        print(num," 175 is not a disarium number")