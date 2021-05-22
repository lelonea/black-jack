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


def game_mode():
    mode = input(
                'Choose game mode:\n'
                '1 - Single player\n'
                '2 - Multiplayer\n'
                '3 - Single player against computer player\n'
                )

    if mode == '1':
        players_number = 1
        return players_number
    elif mode == '2':
        return multi()
    elif mode == '3':
        players_number = 0
        return players_number
    else:
        return 'Wrong input'


def multi():
    try:
        players_number = int(input('Enter number of players (max - 15): \n'))
    except ValueError:
        print('Wrong input')
        return multi()

    if players_number <= 15:
        return players_number
    else:
        print('Maximum number of players is 15, try again')
        return multi()


