import random


INITIAL_STARTING_HAND = 2
DEALERS_STARTING_HAND = 1
WINNING_NUMBER = 21


CARDS = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9":9, "10":10, "J":10, "Q": 10, "K":10}

class BlackJack:
    """Blackjack Card Game - Computer Terminal Style"""
    def __init__(self):
        pass

    def deal_cards(self, hand:list = [], number_of_cards:int=1) -> list:
        """Deals the cards to the player | dealer
        
        :params list hand: takes the initial [ cards in hand | hand in play] and adds to that hand
        :params int number_of_cards: the amount of cards to deal

        :returns hand: the new hand dealt
        """
        for n in range(number_of_cards):
            card = random.choice(list(CARDS.keys()))
            hand.append(card)
        return hand
    
    def flip_ace_value(self, hand) -> int:
        """The current card is an Ace. Flip the card to the desired value"""
        total = self.sum_of_cards(hand) - 10
        return total

    def get_card_value(self, card:str) -> int:
        """Get the current value for the card
        
        :params str, list card: gets the current card from the hand

        :returns: the value of the card 
        """
        # if card is an ace
        if card == 'A':
            return CARDS[card][1]
        return CARDS[card]


    def sum_of_cards(self, hand, ace_flip=False) -> int:
        """Calculates the value of the current hand dealt.
        
        :params list hand: the player | dealers hand.
        :params bool dealer: whether hand is the players | dealers.

        :returns total: the sum of the hand.
        """
        total = 0
        for card in hand:
            if card == "A" and ace_flip:
                card_value = CARDS[card][0]
            else:
                card_value = self.get_card_value(card)
            total+=card_value
        return total
    
    def is_winner(self, total) -> bool:
        """Checks player | dealers hand to see if they won.
        
        :params list hand: the [player | dealer] hand to check
        :params bool dealer: if the hand is for the dealer or player

        :returns tuple | bool: if player | dealer has won, return True and whether it was a player or dealer (else: False)
        """
        if total == WINNING_NUMBER:
            return True 
        return False
     
    def is_draw(self, p_total:int, d_total:int) -> bool:
        """Checks the player and dealers hand to determine if the game is a draw.

        :params list p_hand: the players hand
        :params list d_hand: the dealers hand

        :returns bool: if game is draw, returns True (else: False)

        """
        if p_total == d_total:
            return True
        return False
    
    def is_bust(self, total:int) -> bool:
        """Checks if the total of a hand goes over the winning number"""
        if total > WINNING_NUMBER:
            return True
        return False
    
    def is_greater(self, first_hand_total:int, second_hand_total:int) -> bool:
        """Checks the both hands to see if one was greater than the other"""
        if first_hand_total > second_hand_total:
            return True
        return False
    
    def score(self, p_hand, d_hand, ace_flip) -> tuple:
        """Calculates the final score of both hands"""
        p_total = self.sum_of_cards(p_hand, ace_flip)
        d_total = self.sum_of_cards(d_hand)
        return p_total, d_total


    def game_checks(self, p_total, d_total):
        if self.is_bust(d_total):
            print("Dealer Loses... Player Wins!!")
        elif self.is_winner(d_total):
            print("Dealer Wins!! ... Player Loses..")
        elif self.is_draw(p_total=p_total, d_total=d_total):
            print("DRAW!!!")
        elif self.is_greater(d_total, p_total):
            print("Dealer Wins!!")
        else:
            print("Player Wins!!")