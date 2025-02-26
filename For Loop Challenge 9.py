num = int(input("How many people do you want to invite to a party: "))
if num < 10:
    for i in range(num):
        name = input("Name: ")
        print(name, " has been invited")
else:
    print("Too many people")
        
