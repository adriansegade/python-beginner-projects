from card import Card
from deck import Deck


def main():
    deck = Deck('FRENCH_DECK')
    print(deck.__str__())
    deck.shuffle()
    print(deck.__str__())


if __name__ == '__main__':
    main()
