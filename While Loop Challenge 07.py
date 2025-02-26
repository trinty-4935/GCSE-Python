num = 10

while num > 0:
    print("There are ", num, "green bottles hanging on the wall, ", num, " green bottles hanging on the wall and if one green bottle should accidently fall")
    ans = int(input("How many green bottles would be hanging on the wall?"))
    if ans + 1 == num:
        print("That is correct")
    else:
        while ans + 1 != num:
            ans = int(input("Try again:"))
    num = num - 1
            
