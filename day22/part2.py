#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"


class Player:
    def __init__(self, name: str, cards: List[int]) -> None:
        self.name = name
        self.deck = cards

    @property
    def is_out(self) -> bool:
        return len(self.deck) == 0

    @property
    def score(self) -> int:
        return sum(
            (card * (i + 1))
            for i, card in enumerate(self.deck[::-1])
        )
    
    @property
    def cards_remaining(self) -> int:
        return len(self.deck)

    def play_card(self) -> int:
        assert self.deck
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def take_cards(self, cards: List[int]) -> None:
        self.deck.extend(cards)

    def __repr__(self) -> str:
        return f"{self.name}: {self.deck}"

def play_game(p1: Player, p2: Player) -> Player:  # returns winner
    prev_rounds_of_this_game = set()

    while True:
        card_configuration = (p1.score, p2.score)
        # print(card_configuration)
        if card_configuration in prev_rounds_of_this_game:
            return p1
        else:
            prev_rounds_of_this_game.add(card_configuration)

        if p1.is_out:
            return p2
        elif p2.is_out:
            return p1
        
        p1_card = p1.play_card()
        p2_card = p2.play_card()

        if (p1_card <= p1.cards_remaining) and (p2_card <= p2.cards_remaining):
            _p1 = Player(p1.name, p1.deck[:p1_card])
            _p2 = Player(p2.name, p2.deck[:p2_card])
            round_winner = (
                p1 if (play_game(_p1, _p2) == _p1) else p2
            )
        elif p1_card > p2_card:
            round_winner = p1
        elif p2_card > p1_card:
            round_winner = p2
        else:
            raise RuntimeError('should never hit this!')

        if round_winner == p1:
            p1.take_cards([p1_card, p2_card])
        elif round_winner == p2:
            p2.take_cards([p2_card, p1_card])
        else:
            raise RuntimeError('should never hit this!')


if __name__ == "__main__":
    p1_cards = []
    p2_cards = []
    with open(PUZZLE_INPUT) as f:
        f.readline()
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            p1_cards.append(int(line))
        
        f.readline()
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            p2_cards.append(int(line))

    p1 = Player("Player1", p1_cards)
    p2 = Player("Player2", p2_cards)

    winner = play_game(p1, p2)
    print(winner.score)
