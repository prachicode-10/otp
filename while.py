# i = 1
# while i <= 10:
#     print('*' * i)
#     i = i + 1
# print("This is a while loop")

# guessing game

# num = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess a number between 1 and 10: "))  
#     guess_count += 1
#     if guess == num:
#         print("You guessed it right!")
#         break
#     else: 
#         print("Wrong guess, try again!")    


command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print (""" 
start - to start the car
stop - to stop the car
quit - to quit
        """)

    elif command == "quit":
        break
    else: 
        print ("sorry i dont understand")