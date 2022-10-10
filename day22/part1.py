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

    def play_card(self) -> int:
        assert self.deck
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def take_cards(self, cards: List[int]) -> None:
        self.deck.extend(cards)

    def __repr__(self) -> str:
        return f"{self.name}: {self.deck}"


def play_game(p1: Player, p2: Player) -> int:  # returns score of winner
    while True:
        if p1.is_out:
            return p2.score
        elif p2.is_out:
            return p1.score
        
        p1_card = p1.play_card()
        p2_card = p2.play_card()

        if p1_card > p2_card:
            p1.take_cards([p1_card, p2_card])
        elif p2_card > p1_card:
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

    winning_score = play_game(p1, p2)
    print(winning_score)
