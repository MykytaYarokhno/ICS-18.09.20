from dataclasses import dataclass
import random

suits = ['Diamond','Heart','Spade','Club']

@dataclass
class Card:
    suit: str
    number: int

class CardDeck():
    
    def __init__(self):
        self.card_deck_array = []
        
        for suit in suits:
            for card in self.create_suit_pack(suit):
                self.card_deck_array.append(card)


        random.shuffle(self.card_deck_array)

    def create_suit_pack(self, suit_name):
        suit_pack = []
        for i in range(2, 14):
            suit_pack.append(Card(suit_name, i))

        return suit_pack

    def print_card_deck(self):
        print('Print all cards ' + str(self.card_deck_array))

    def get_card_by_id(self, id):
        return self.card_deck_array[id - 1]

    def shuffle_deck(self):
        random.shuffle(self.card_deck_array)

    def get_card(self):
        card = self.card_deck_array[0]
        self.card_deck_array.remove(card)

        return card

    def get_six_cards(self):
        six_cards = [
            self.card_deck_array[0],
            self.card_deck_array[1],
            self.card_deck_array[2],
            self.card_deck_array[3],
            self.card_deck_array[4],
            self.card_deck_array[5],
            ]

        for card in six_cards:
            self.card_deck_array.remove(card)

        return six_cards

card_deck = CardDeck()
card_deck.print_card_deck()
print('\n')
print('Give fourth card from deck ' + str(card_deck.get_card_by_id(4)) + "\n")
card_deck.print_card_deck()
print('\n')
print('Shuffle cards \n')
card_deck.shuffle_deck()
card_deck.print_card_deck()
print('\n')
print('Give one card ' + str(card_deck.get_card()) + '\n')
print('Give six cards ' + str(card_deck.get_six_cards()))
        
        
