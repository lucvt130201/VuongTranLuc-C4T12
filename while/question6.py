print("How many legs does a spider has?")
print("1. none")
print("2. 4 legs")
print("3. 8 legs")
print("4. 12 legs")

# if ans == 3:
#     print("Correct!")
while True:
    ans = input("Your answer: ")
    if ans.isdigit() == True:
        ans = int(ans)
        if ans == 3:
            print("Correct!")
            break
        elif ans >= 1 and ans <= 4 and ans != 3:
            print("Your ans is:", ans)
            print("Wrong! The answer is 3")
            break
        else:
            print("your ans must be 1, 2, 3 or 4 only. Please enter again.")

    if ans.isdigit() == False:
        print("your ans must be 1, 2, 3 or 4 only. Please enter again.")
        
    