
# WELCOME TO BLACKJACK GAMES CENTRAL!
        # Instructions: You and the dealer are dealt two cards each, while the dealer is dealt one face up. 
        # If your first 2 cards add up to 21 , that's Blackjack! 
        # If they have any other total, decide whether you wish to 'stand' or 'hit'. 
        # You can continue to draw cards until you are happy with your hand.

# Using "random" library in order to randomly select a card from the deck, import os in order to allow everything to operate with eachother
import random

#opening prompt + asking if player if they would like to play
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

#indicating the player and dealer are playing
player_In = True
dealer_In = True

#created a list of the deck then adding them into the player and dealer hand 

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K']

playerHand = []
dealerHand = []

# used shuffle to shuffle the deck, apppend to add the card to the deck, then remove to remove the card from the deck
def dealCard(turn):
    card = random.choice(deck)
    random.shuffle(deck)
    turn.append(card)
    deck.remove(card)

# changing the non-integer deck items into 
def total(turn):
    total = 0
    face = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

#function in order to always mask one card in the dealers hand
def revealDealerHand(hand):
    masked_hand = hand.copy()
    masked_hand[0] = create_mask(masked_hand[0])
    return masked_hand

def create_mask (string_to_mask, masking_char = "?"):
    string_to_mask = str(string_to_mask)
    mask = len(string_to_mask) * masking_char
    return mask
# testing the mask
# print(create_mask("1"))
# create_mask("ace", "x")
       
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

#prompt asked in order to determine if player wants to draw another card or to stand
while player_In or dealer_In:
    print(f"Dealer had {revealDealerHand(dealerHand)}")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if player_In:
        stayOrhit = input("1: Stand\n2: Hit\n")
    if stayOrhit == '2':
        dealCard(dealerHand)
        dealCard(playerHand)
    if stayOrhit == '1':
        dealCard(dealerHand)
    if total(dealerHand) > 21:
        break
    if total(playerHand) < 21 and total(dealerHand) < 21:
        continue
    if total(playerHand) or total(dealerHand) >= 21:
        break

# the possibilities of game outcomes and the meanings/winners
if total(playerHand) == 21:
    print(f"\n{name} has {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You Win! You got Blackjack!🥳")
elif total(dealerHand) == 21:
    print(f"\n{name} has {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print(" Dealer got Blackjack! You lose😭")   
elif total(playerHand) > 21 and total(dealerHand) < 21:
    print(f"\n{name} has {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You busted! Dealer wins!😅") 
elif total(dealerHand) > 21 and total(playerHand) < 21:
    print(f"\n{name} has {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print( "You win, Dealer busted!😁")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer Wins! You lose😢")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You Win! Dealer loses😎")    
elif total(playerHand) > 21 and total(dealerHand) > 21:
    print(f"\n{name} has {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print(" Its a tie!🧐") 
