# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     print(i)

# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         print(str(i) + " is even.")
#     # else:
#     #     print(str(i) + " is odd.")


# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(str(number) + " x " + str(i) + " = " + str(number * i))


# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print("Sum of numbers from 1 to 100: " + str(sum))


# password = "behlol123"
# userInput = input("Enter the password: ")

# while userInput != password:
#     print("Incorrect password. Please try again.")
#     userInput = input("Enter the password: ")

# print("Access granted. Welcome!")

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()