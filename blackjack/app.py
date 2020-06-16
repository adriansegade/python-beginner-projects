from card import Card

try:
    card = Card('spades', )
except Exception as e:
    print(f'Exception when creating card: {e}')
