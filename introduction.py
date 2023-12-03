#file for opening prompt and game introduction

print("Welcome to our Game of Blackjack!")
name = input("What is your name? ") 
print("Hello " + name + "!")

choice = input("Are you ready to play? (Y/N) : ").lower()
if choice == "y":
    print("Lets get started " + name + "!")
else: 
    print("Entry must be either Y or N")
    print("No worries, bye bye 👋!")
    exit()
    
