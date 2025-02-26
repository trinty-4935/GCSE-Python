total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    yon = input("Do you want to keep this number(y/n)?: ")
    if yon == "y":
        total = total + num
print(total)
        
