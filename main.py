#FUNCTIONS AND VARIABLES NEEDED TO SUPPORT GAME
import random
dealer = []
player = []
dealer_total = 0
player_total = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
#what's going on with L77?

def game_start():
    ready = input("When you are ready to start, type deal and then press enter/return. \n")
    if ready == "deal":
        deal()
    else:
        print("Sorry you're response was not recognized")

def deal():
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))
    print(f"The dealer's hand is {dealer}.")
    print(f"The player's hand is {player}.")
    if sum(dealer) == 21 and sum(player) == 21:
        print("The game is a draw!")
        play_again()
    elif sum(dealer) == 21 and sum(player) != 21:
        print("The dealer has 21 and wins the game. ")
        play_again()
    elif sum(dealer) != 21 and sum(player) == 21:
        print("You have 21 and win the game. ")
        play_again()

def who_wins():
    player_total == sum(player)
    dealer_total == sum(dealer)
    if player_total > dealer_total:
        print("You had the higher hand.  You win the game")
        play_again()
    elif player_total < dealer_total:
        print("The dealer has the higher hand.  You loose the game")
        play_again()
    elif player_total == dealer_total:
        print("The game is a draw!")
        play_again()

def play_again():
    dealer = []
    player = []
    dealer_total = 0
    player_total = 0
    game_again = input("Would you like to play again")
    if game_again == yes:
        deal()
    else:
        print("Thank you for playing.  I hope you enjoyed the game.")


game_over = False

game_again = ""




game_start()

while game_over == False:
    choice = input("Would you like to hit or stay? \n")
    if choice == "hit":
        player.append(random.choice(cards))
        if sum(player) >= 22:
            print(f"{player} Sorry, you are over 21 and you loose.")
            play_again()
        elif sum(player) <=21:
            print(f"Your hand is now {player} "
    elif sum(dealer) <= 15:
        dealer.append(random.choice(cards))
        if sum(dealer) >= 22:
            print(f"{dealer} The dealer has gone over 21 and you win")
            play_again()
        else:
            print(dealer)
            who_wins()
    else:
        who_wins()



