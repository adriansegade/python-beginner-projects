class Card:
    
    AVAILABLE_SUITS = ('hearts', 'diamonds', 'clubs', 'spades')
    AVAILABLE_FACE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k')
    VALUES = ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    def __init__(self, suit, face):
        if suit in self.AVAILABLE_SUITS:
            if face in self.AVAILABLE_FACE:
                self.suit = suit
                self.face = face
            else:
                raise ValueError('Invalid value')
        else:
            raise ValueError('Invalid suit')

    def __str__(self):
        return f'{str(self.face).upper()}{self.suit[0].upper()}'
