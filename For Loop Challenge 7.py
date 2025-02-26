direction = input("What whay do you want to count? (u/d): ")
if direction == "u":
    num = int(input("Enter a number: "))
    num1 = num
    for i in range(num):
        print(num - num1 + 1)
        num1 = num1 - 1
elif direction == "d":
    num = int(input("Enter a number below 20: "))
    num1 = 20 - num
    num3 = num1 + 1
    num2 = 20
    for i in range(num3):
        print(num2)
        num2 = num2 - 1
else:
    print("I don't understand")
    
