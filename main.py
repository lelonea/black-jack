from random import shuffle


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
        shuffle(self.cards)

    def take_card(self):
        try:
            card = self.cards.pop(0)
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

    @staticmethod
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
            return BigDeck.choose_deck()


class AllPlayers:
    deck = BigDeck.choose_deck()
    players_list = []

    def __init__(self, name):
        self.name = name
        self.players_list.append(self.name)
        self.cards = [self.deck.take_card(), self.deck.take_card()]
        self.position = None

    def ask_card(self, deck):
        card = deck.take_card()
        self.cards.append(card)


class Bot(AllPlayers):
    pass


class Player(AllPlayers):
    pass


class Game:
    def __init__(self):
        self.players_number = 1
        self.players = []
        self.players_names = []

    def start_game(self):
        while self.players_number > 0:
            inp_name = input("Enter player's name: ")
            self.players_names.append(inp_name)
            inp_name = Player(inp_name)
            self.players.append(inp_name)
            self.players_number -= 1

    def game_mode(self):
        mode = input(
            'Choose game mode:\n'
            '1 - Single player\n'
            '2 - Multiplayer\n'
            '3 - Single player against computer player\n\n'
            'ENTER: '
        )

        if mode == '1':
            self.players_number = 1
        elif mode == '2':
            return self.multi()
        elif mode == '3':
            self.players_number = 1
            b = Bot('Bot')
            self.players.append(b)
        else:
            return 'Wrong input'

    def multi(self):
        try:
            self.players_number = int(input('Enter number of players (max - 6): \n'))
        except ValueError:
            print('Wrong input')
            return self.multi()

        if self.players_number <= 6:
            return self.players_number
        else:
            print('Maximum number of players is 6, try again')
            return self.multi()




