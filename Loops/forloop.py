# Wap to print the total number of prime number between 1 -100




countPrime = 0 #0
sumPrime = 0 #11
ProductPrime = 1
for j in range(1, 101) :
    if j>1:
        num = j #2
        checkPrime = True
        for i in range(2, num) :
            if num%i==0:
                checkPrime = False
                break
        if checkPrime==True:
            print(num)
            countPrime = countPrime=1
            sumPrime = sumprime=num
            productPrime = ProductPrime*num

print("The total number of prime number between 1-100 : " ,countPrime)
print("The sum  of prime number between 1-100 : " ,sumPrime)
print("The product of prime number between 1-100 : " ,ProductPrime)