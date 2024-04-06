#conditional statement
# age = int(input("Enter the age"))
# if age >=18:
#     print("you are eligible for vote")
# else:
#     print("Not eligible for voting")

# write a programm to check whether a number entered by user is even or odd
# num = int(input("Enter the num"))
# if num%2==0:
#     print("num is even")
# else:
#     print("num is odd")


# num  = int(input("enter a num"))
# if num%7==0:
#     print("number is divisible by 7")
# else:
#     print("number is not divisible by 7")


# amt = 0
# x = int(input("Enter the num"))
# if x<=100:
#     amt=0
# if x>100 and x<=200:
#     amt=(x-100)*5
# if x>200:
#     amt=500+(x-200)*10
# print("Amount to pay :" ,amt)


# num2 = int(input("Enter a number"))
# num1 = int(input("Enter a number"))
# if num1>num2:
#     print("num1 is greter the num2")
# elif num1<num2:
#     print("num1 is less the num2")
# else:
#     print("num1 is equal the num2")

# quantity = int(input("Enter the quantity"))
# total_cost = quantity*100
# if  total_cost>1000:
#     discount = 0.1*total_cost
#     total_cost -= discount
# else:
#     print("total cost")
# print("total cost :",total_cost)


# 2) A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years.
# Ask users for their salary and year of service and print the net bonus amount.

# age = int(input("Enter the age"))
# sex = input("Enter the sex")
# matital_status = input("enter the status")
# if sex == "F":
#     print("you will work in urban areas")
# elif sex == "M":
#     if 20<= age <= 40:
#         print("You may in anywhere")
#     elif 40<= age <= 60:
#         print("you will work in urban areas only")
#     else:
#         print("ERROR: Invalid age")
# else:
#         print("ERROR: Invalid age")

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n, end=' ')

# Call the function to print numbers from 1 to 100
print_numbers(100)






