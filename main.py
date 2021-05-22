class SmallDeck:
    def __init__(self):
        self.cards = [6, 7, 8, 9, 10, 'Jack', 'Lady', 'King', 'Ace'] * 4


class BigDeck(SmallDeck):

    addition = [2, 3, 4, 5] * 4

    def __init__(self):
        super().__init__()
        self.cards.extend(self.addition)



