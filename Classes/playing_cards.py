from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = 'clover diamond heart spade'.split()


def make_french_deck():
    return [PlayingCard(r, s) for r in RANKS for s in SUITS]


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    # __str__() method is not implemented in data classes. they return a user friendly representation of obj
    def __str__(self):
        return f'{self.suit} {self.rank}'

    def __post_init__(self):
        self.sort_index = RANKS.index(
            self.rank) * len(SUITS) + SUITS.index(self.suit)


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        """!s following c means that we'd like to use the str method of Playing card class"""
        cards = ','.join(f'{c!s}' for c in self.cards)
        return f'{cards}'


# two_cards = Deck([queen_of_hearts, ace_of_spades])


# print(Deck())


# def create_multipliers():
#     multipliers = []

#     for i in range(5):
#         def multiplier(x):
#             return i * x
#         multipliers.append(multiplier)
#     return multipliers

# def create_multipliers():
#     return [lambda x, i=i: i * x for i in range(5)]


card = PlayingCard('Q', 'heart')
print(RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit))
queen_of_hearts = PlayingCard("Q", "heart")
ace_of_spades = PlayingCard("A", "spade")
print(ace_of_spades > queen_of_hearts)
# sorted_deck = Deck(sorted(make_french_deck()))
# print(sorted_deck)
print(queen_of_hearts)
print(Deck())
