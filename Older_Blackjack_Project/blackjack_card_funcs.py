import random

# Choose New Card
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_hand(hand:list, num:int):

    """This function deals the cards for playing blackjack"""
    
    # remember to go back to datacamp & udemy notes to review docstrings and notation ettiquite
    # place them within triple quotes in this bock preceding code
    # !!!!
    
    for n in range(num):
        card = random.choice(cards)
        hand.append(card)

    return hand





def deal_hand(hand:list, player_stayed:bool):

    """This function works specifically for the computer for recursive list append"""

    # remember to go back to datacamp & udemy notes to review docstrings and notation ettiquite
    # place them within triple quotes in this bock preceding code
    # !!!!
    
    plyr_stay = player_stayed
    
    while plyr_stay:
        card = random.choice(cards)
        hand.append(card)
        if sum(hand) >= 17:
            plyr_stay = False

    return hand




# new function that takes the sum of a hand and compares the values with that of another

def compare_cards(p_cards, d_cards):
    """This function returns the sum of the winning hand"""
    if sum(p_cards) == sum(d_cards):
        print("DRAW!!")
    elif sum(d_cards) > 21:
        print("Dealer Bust!, You Win!")
    elif sum(p_cards) > 21:
        print("Bust!\nDealer Wins, You Lose!")
    elif sum(p_cards) == 21:
        print("You Win!")
    elif sum(p_cards) > sum(d_cards):
        print("You Win!")
    else:
        print("Dealer Wins!")
        
    
        
        









        
        
