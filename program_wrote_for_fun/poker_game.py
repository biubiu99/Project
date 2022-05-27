from typing import List, Tuple, Dict


class Card:
    def __init__(self, suit: str, value: int):
        self.suit: str = suit
        self.value: int = value

    def __repr__(self) -> str:
        if self.value == 14:
            self.string = "A"
        elif self.value == 13:
            self.string = 'K'
        elif self.value == 12:
            self.string = 'Q'
        elif self.value == 11:
            self.string = 'J'
        else:
            self.string = str(self.value)
        return f'{self.string}{self.suit}'

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value


class Deck:

    def __init__(self):
        self.deck: List[Card] = []
        for suit in ['H', 'D', 'S', 'C']:
            for value in range(2, 15):
                self.deck.append(Card(suit, value))
        self.removed_cards = []

    def shuffle(self):
        """

        :return: shuffle the deck so the order is random
        """
        from random import shuffle

        shuffle(self.deck)

    def deal_card(self):
        """

        :return: the first card from the deck
        """

        return self.deck.pop(0)

    def deal_cards(self, number: int):
        """
        :return: deal multiple cards from this deck
        """
        cards = []
        for i in range(number):
            cards.append(self.deal_card())
        return cards

    def removed_cards(self):
        return self.removed_cards().append(self.deal_cards())

    def deal_hand(self) -> List[Card]:
        """

        :return: 5 cards from the deck
        """

        return self.deal_cards(5)

    def restart(self):
        prompt = 'Do you want to get different cards? Enter Y for yes and N for no'
        error_prompt = 'Please enter Y or N'
        user_input: str = input(prompt)
        while True:
            try:
                if user_input == 'Y':
                    self.deck.extend(self.removed_cards)
                    self.removed_cards.clear()
                    self.shuffle()
                    print(len(self.deck))
                    n_cards = input('How many of cards you want to get?')
                    print(self.deal_cards(int(n_cards)))
                    break
                elif user_input == 'N':
                    print(self.removed_cards)
                    break
            except Exception: #Why this does not work?
                print(error_prompt)

class Hand:
    def __init__(self,cards: List[Card]):
        self.cards: List[Card] = sorted(cards)
        self.value: int = self.compute_value()

    def __repr__(self):
        result = ''
        for card in self.cards:
            result += f'{card}'
        return result[-1]


    def count_value_rank(self) -> Dict[int,int]:
        ranks:  Dict[int,int] = {}
        for card in self.cards:
            if card.value in ranks:
                ranks[card.value] += 1
            else:
                ranks[card.value] = 1

        return ranks

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def count_suit_rank(self) -> Dict[str,int]:
        ranks: Dict[str,int] = {}
        for card in self.cards:
            if card.suit in ranks:
                ranks[card.suit] += 1
            else:
                ranks[card.suit] = 1
        return ranks


    def hand_ranking(self):
        value_rank: Dict[int,int] = self.count_value_rank()
        if len(value_rank) == 5: #it can be flush/royal flush
            return 0
        elif len(value_rank) == 4:
            return 1
        elif len(value_rank) == 3:
            #1,1,3 or 1,2,2
            if 2 in value_rank.keys(): #3 of a kind
                return 3
            else:
                return 2 # 2 pairs
        elif len(value_rank) == 2:
            #2,3 or 1,4
            if 3 in value_rank:
                return 6 # full house
            else: # 4 of a kind
                return 7

    def is_flush(self) -> bool:
        suit_rank: Dict[str,int] = self.count_suit_rank()
        if len(suit_rank) == 1:
            return True
        else:
            return False

    def is_straight(self) -> bool:
        min_value: int = self.cards[0].value
        max_value: int = self.cards[-1].value
        straight_list: List[int] = list(range(min_value,max_value + 1))
        for i, card in enumerate(self.cards):
            if card.value != straight_list[i]:
                return False
        return True

    def is_straight_flush(self) -> bool:
        return self.is_straight() and self.is_flush()

    def is_royal_flush(self) -> bool:
        return self.is_straight_flush() and self.cards[-1].value == 14

    def compute_value(self):
        hand_rank = self.hand_ranking()
        is_flush = self.is_flush()
        is_straight = self.is_straight()
        is_straight_flush = self.is_straight_flush()
        is_royal_flush = self.is_royal_flush()

        if hand_rank == 0:
            return self.cards[-1].value
        elif hand_rank == 1:
            return 14 + self.cards[-1].value
        elif hand_rank == 2:
            return 28 + self.cards[-1].value
        elif hand_rank == 3:
            return 42 + self.cards[-1].value
        elif is_straight:
            return 56 + self.cards[-1].value
        elif is_flush:
            return 70 + self.cards[-1].value
        elif hand_rank == 6:
            return 84 + self.cards[-1].value
        elif hand_rank == 7:
            return 98 + self.cards[-1].value
        elif is_straight_flush:
            return 112 + self.cards[-1].value
        elif is_royal_flush:
            return 126

def main():
    my_deck: Deck = Deck()
    my_deck.shuffle()
    my_hand: Hand = my_deck.deal_hand()
    other_hand: Hand = my_deck.deal_hand()
    print(other_hand)

if __name__ == '__main__':
    main()














