from card import Card
from random import seed, randint

class Deck:
    DECKS = {
        'FRENCH_DECK': {
            'suits':  ('hearts', 'diamonds', 'clubs', 'spades'),
            'faces': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k')
        }
    }

    def __init__(self, type):
        if type in self.DECKS.keys():
            self.deck = []
            for suit in self.DECKS[type]['suits']:
                for face in self.DECKS[type]['faces']:
                    self.deck.append(Card(suit, face))

    def __str__(self):
        r = ''
        deck = self.deck[:-1]
        for card in deck:
            r += f'{card.__str__()}, '
        r += self.deck[-1:][0].__str__()
        return r

    def shuffle(self):
        # random.shuffle(self.deck) would also work
        temp = []
        while len(self.deck) > 0:
            seed()
            index = randint(0, len(self.deck) - 1)
            temp.append(self.deck[index])
            del self.deck[index]
        self.deck = temp

