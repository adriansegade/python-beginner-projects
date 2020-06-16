class Card:
    
    AVAILABLE_SUITS = ('hearts', 'diamonds', 'clubs', 'spades')
    AVAILABLE_VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k')

    def __init__(self, suit, value):
        if suit in self.AVAILABLE_SUITS:
            if value in self.AVAILABLE_VALUES:
                self.suit = suit
                self.value = value
            else:
                raise ValueError('Invalid value')
        else:
            raise ValueError('Invalid suit')