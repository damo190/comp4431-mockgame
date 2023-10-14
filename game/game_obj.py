from entities import Player, Boss, Entity
from cards.card_list import card_catalog


class Game:
    players: list[Player] = []
    bosses: Boss = []
    curr_boss: Boss = None
    turn: int = 0
    max_turns: int = 0

    def __init__(self, num_players, max_turns) -> None:
        self.players = []
        self.bosses = []
        self.curr_boss = None
        self.turn = 0
        self.max_turns = max_turns

        for num in range(num_players):
            self.players.append(Player(card_catalog, "player" + str(num + 1)))
        self.bosses.append(Boss())
        self.curr_boss = self.bosses[0]

    def __str__(self) -> str:
        ret = "Game State: \n"
        ret += "\n Boss Status: "
        ret += "\n\t" + str(self.curr_boss)

        return ret
    
    def print_players(self) -> None:
        ret = ""
        ret += "\nPlayers:\n\n"
        for p in self.players:
            ret += str(p) + "\n"
        print(ret)

    def find_player(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None

    

    def all_entities(self) -> list[Entity]:
        e = []
        for p in self.players:
            e.append(p)
        e.append(self.curr_boss)
        return e

    def turn_reset(self):
        for e in self.all_entities():
            e.modifier = 0
            e.shield = 0

