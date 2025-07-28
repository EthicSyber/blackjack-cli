from blackjack_card_funcs import play_hand, deal_hand, compare_cards
from blackjack_art import blackjack_logo as logo
import random


def blackjack_card_game():
    """Starts the blackjack game"""
    # blackjack game is active
    blackjack = True
    
    # create both players and dealers first hand
    players_hand = play_hand([], 2) # this will give the first pair
    dealers_hand = play_hand([], 1) # this will start off the dealer (computer) hand with a card

    # print logo
    print(logo)

        
    while blackjack:

        print(f"Your cards: {players_hand}, current score: {sum(players_hand)}")
        print(f"Computers first card: {dealers_hand[0]}")
        
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            players_hand = play_hand(players_hand, 1)
            if sum(players_hand) > 21:
                print("Bust!\nDealer Wins, You Lose!")
                blackjack = False
        else:
            dealers_hand = deal_hand(dealers_hand, True)
            compare_cards(players_hand, dealers_hand)
            blackjack = False
        
      
        
    print(f"Your final hand: {players_hand}, final score: {sum(players_hand)}")
    print(f"Computers final hand: {dealers_hand}, final score: {sum(dealers_hand)}")

    play_again = input("Would you like to play again?: ").lower()
    if play_again == 'y':
        print('\n' * 30)
        blackjack_card_game()


blackjack_card_game()

