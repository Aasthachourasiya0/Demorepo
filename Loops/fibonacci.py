n = int(input("Enter number of term"))
a = 0
b = 1
s = 0

for i in range(n):
    print(s,end=" ")
    s = a+b
    b = a
    a =s


# for j in range(10,10000):
#     num = j
#     t1 = num 

#     digits = 0  #4
#     while(t1>0): #0
#         digits+=1
#         t1//=10

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
        print(num,"is an fibonacci number")
