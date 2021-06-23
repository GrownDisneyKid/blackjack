#FUNCTIONS AND VARIABLES NEEDED TO SUPPORT GAME
import random
dealer = []
player = []

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal():
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    print(f"The dealer's hand is {dealer}.")
    print(f"The player's hand is {player}.")

def choice():
    decision = input("Whould you like to hit or stand? ")
    if decision == "hit":
        player.append(random.choice(cards))
    else:
        who_wins()


def players_totals():
    for n in player:
        player_total += n
        print(f"The player's total is {player_total}. ")

#def who_wins():
    #


#import art
#print logo


# ask play if they are ready to deal cards
ready = input("When you are ready to start, type start and then press enter/return" )

if ready == "start":
    deal()
else:
    print("Sorry you're response was not recognized")


# issues two random cards to each player

deal()

# evaluate totals and if players are over 21

players_totals()

# combine dealer and player lists for total
#evaluate to see if either is over 21

# deal additional cards to each player

#evaluate totals and if anyone is over 21

# present the winner or declare a draw

