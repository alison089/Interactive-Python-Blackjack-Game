#file for opening prompt and game introduction

print("Welcome to our Game of Blackjack!")
name = input("What is your name? ") 
print("Hello " + name + "!")

while True:
    try:
        choice = int(input("Are you ready to play? (1: Y/ 2: N) : "))
        assert (int(choice) < 1 )
        assert(int(choice) > 2)
        break
    except ValueError:
        print("please enter a number")
    except:
        ("please enter 1: Yes or 2: No")
    break
if choice == 2:
    print("Oh No! Have a good one! Bye Bye!")
    exit()
