import random


class SmallDeck:
    def __init__(self):
        self.cards = [6, 7, 8, 9, 10, 'Jack', 'Lady', 'King', 'Ace'] * 4
        self.values = {}
        for i in set(self.cards):
            if type(i) == int:
                self.values[i] = i
            elif i == 'Ace':
                self.values[i] = 11
            else:
                self.values[i] = 10

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def take_card(self):
        try:
            card = self.shuffle().pop(0)
            value = self.values[card]
        except IndexError:
            return 'Deck is empty'
        return card, value


class BigDeck(SmallDeck):

    addition = [2, 3, 4, 5] * 4

    def __init__(self):
        super().__init__()
        self.cards.extend(self.addition)
        for i in set(self.addition):
            self.values[i] = i


def choose_deck():
    choose = input(
                   'Choose deck to play:\n'
                   '1 - Small deck 36 cards\n'
                   '2 - Big deck 52 cards\n\n'
                   'ENTER: '
                   )

    if choose == '1':
        return SmallDeck()
    elif choose == '2':
        return BigDeck()
    else:
        print('\nWrong input, try again\n')
        return choose_deck()


