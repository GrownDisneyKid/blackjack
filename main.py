#FUNCTIONS AND VARIABLES NEEDED TO SUPPORT GAME
import random
dealer = []
player = []
dealer_total = 0
player_total = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]

def deal():
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    print(f"The dealer's hand is {dealer}.")
    print(f"The player's hand is {player}.")

game_over = False

# def choice():
#     decision = input("Whould you like to hit or stand? ")
#     if decision == "hit":
#         player.append(random.choice(cards))
#     else:
#         who_wins()

ready = input("When you are ready to start, type deal and then press enter/return. \n")

if ready == "deal":
    deal()
else:
    print("Sorry you're response was not recognized")


while game_over != True:
    choice = input("Would you like to hit or stay? \n")
    if choice == "hit":
        player.append(random.choice(cards))
        if sum(player) >= 22:
            print(f"{player} Sorry, you are over 21 and you loose.")
            game_over = True
        elif choice == "stay":
           print(player)
    elif sum(dealer) <= 16:
        dealer.append(random.choice(cards))
        if sum(dealer) >= 22:
            printf("{dealer} The dealer has gone over 21 and you win")
            game_over = True
        else:
            print(dealer)
    else:
        who_wins()

# def players_totals():
#     for n in player:
#         player_total = sum(player)
#     for o in dealer:
#         dealer_total = sum(dealer)
#     print(f"The player's total is {player_total}. ")
#     print(f"The player's total is {dealer_total}. ")

#def who_wins():
    #


#import art
#print logo


# ask play if they are ready to deal cards



# issues two random cards to each player



# evaluate totals and if players are over 21


# combine dealer and player lists for total
#evaluate to see if either is over 21

# deal additional cards to each player

#evaluate totals and if anyone is over 21

# present the winner or declare a draw

