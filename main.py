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


class Game:
    def __init__(self):
        self.deck = self.choose_deck()
        self.mode = self.game_mode()

    def choose_deck(self):
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
            return self.choose_deck()

    def game_mode(self):
        mode = input(
            'Choose game mode:\n'
            '1 - Single player\n'
            '2 - Multiplayer\n'
            '3 - Single player against computer player\n\n'
            'ENTER: '
        )

        if mode == '1':
            players_number = 1
            return players_number
        elif mode == '2':
            return self.multi()
        elif mode == '3':
            players_number = 0
            return players_number
        else:
            return 'Wrong input'

    def multi(self):
        try:
            players_number = int(input('Enter number of players (max - 15): \n'))
        except ValueError:
            print('Wrong input')
            return self.multi()

        if players_number <= 15:
            return players_number
        else:
            print('Maximum number of players is 15, try again')
            return self.multi()


class Player:
    players_list = []
    game = Game()
    deck_to_play = game.deck
    player_number = game.mode

    def __init__(self, name='Name'):
        self.name = name
        self.players = self.players_list.append(self.name)
        self.cards_in_hand = [self.deck_to_play.take_card(), self.deck_to_play.take_card()]

    def take_card(self):
        self.cards_in_hand.append(self.deck_to_play.take_card())


