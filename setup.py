from blackjack import BlackJack
from game_art import blackjack_logo

INITIAL_STARTING_HAND = 2
DEALERS_STARTING_HAND = 1
HIT = 1

def blackjack():
    game = BlackJack()
    game_on = True
    players_hand = game.deal_cards([], number_of_cards=INITIAL_STARTING_HAND)
    dealers_hand = game.deal_cards([], number_of_cards=DEALERS_STARTING_HAND)

    ace_flip = False

    p_total = 0
    d_total = 0

    print('\n' * 30)
    print(blackjack_logo)
    while game_on:
        # display both card hands
        print("Dealer's Hand: ", dealers_hand)
        print("Player's Hand:", players_hand)
        print("\n")

        # Players Hand 
        if not ace_flip and "A" in players_hand and input("Want to flip your Ace? (current-value: 11) Type [ yes | no ]: ").lower().startswith('y'):
            ace_flip = True

        get_card = input("Do you want to hit or stay? Type [ hit | stay ]: ").startswith('h')
        print("\n")
        if get_card:
            players_hand = game.deal_cards(players_hand, number_of_cards=HIT)
            p_total = game.sum_of_cards(hand=players_hand, ace_flip=ace_flip)
            
        # Dealers Hand
        else:
            player_stayed = True
            while player_stayed:
                dealers_hand = game.deal_cards(dealers_hand, number_of_cards=HIT)
                # dealer stays; break loop
                if game.sum_of_cards(dealers_hand) >= 17:
                    player_stayed = False

            # gets score; performs final checks
            p_total, d_total = game.score(p_hand=players_hand, d_hand=dealers_hand, ace_flip=ace_flip)
            game.game_checks(p_total, d_total)
            game_on = False
        
        if game.is_bust(p_total):
            print("Bust!!, Dealer Wins!")
            game_on = False
        elif game.is_winner(p_total):
            print("Player Wins")
            game_on = False

    print("\n")

    p_total, d_total = game.score(p_hand=players_hand, d_hand=dealers_hand, ace_flip=ace_flip)
    print("Dealer:", dealers_hand, d_total)
    print("Player: ", players_hand, p_total)
    print("\n")

    play_again = input("Would you like to play again? Type [ yes | no ]: ").lower().startswith('y')
    if play_again:
        blackjack()
    


