# for num in range(1, 11):
    
#    if num % 2 == 0:
#     print(num)    
  
# num = int(input("Enter a number: "))
# for fact in range(1, num + 1):
#     if num % fact == 0:
#         print(fact)

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)
#         count = count +1
#         if count == 2:
#             print("Prime")
#             break

# num = int(input("Enter a number: "))
# count = 0   
# while num!= 0:
#     dig = num%10
#     num = num // 10
#     count = count +1
#     print("The number of digits is:", count)

# for row in range(1,5):
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()

# for i in range (1,5):
#     while (i>0):
#         print("*", end=" ")
#         i = i -1
#     print()

# for row in range(1,5):
#     print("*" * row)

#pallindrome number

# Program to check if a number is a palindrome

# num = int(input("Enter a number: "))
# num1 = num #original value
# num2 = 0 #revrsed value will store here

# while num > 0:
#     digit = num % 10
#     num2 = num2 * 10 + digit
#     num = num // 10

# if num1  == num2:
#     print("Yes! It's a palindrome number.")
# else:
#     print("No, it's not a palindrome.")


a= int(input("Enter a number: "))
b= int(input("Enter another number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print("The sum is:", a + b)
elif operator == "-":
    print("The difference is:", a - b)
elif operator == "*":
    print("The product is:", a * b)
elif operator == "/":
    if b != 0:
        print("The quotient is:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")