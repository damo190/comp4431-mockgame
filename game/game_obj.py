from entities import Player, Boss, Entity, Card, CardType, CardTarget
from cards.card_list import create_deck
from boss.scarecrow import Scarecrow
from boss.deranged_cow import DerangedCow
from boss.innocent_lamb import InnocentLamb
from boss.phat_piggy import PhatPiggy


class Game:
    players: list[Player] = []
    bosses: list[Boss] = []
    deck: list[Card] = []
    exec_queue: list[dict] = []
    holiday: list[Player] = []
    curr_boss: Boss = None
    turn: int = 0
    max_turns: int = 0
    simulator = None

    def __init__(self, num_players, max_turns, simulator) -> None:
        self.players = []
        self.bosses = []
        self.exec_queue = []
        self.total_bosses = 4
        self.curr_boss = None
        self.turn = 0
        self.max_turns = max_turns
        self.simulator = simulator
        self.deck = create_deck()
        for num in range(num_players):
            self.players.append(Player(self.deck, "player" + str(num + 1), max_turns))
        self.bosses = [Scarecrow(), DerangedCow(), InnocentLamb(), PhatPiggy()]
        self.curr_boss = self.bosses.pop(0)

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

    def players_draw(self):
        for p in self.players:
            num_cards = len(p.hand)
            if len(self.deck) < 5 - num_cards:
                self.deck = create_deck()
            p.draw_card(self.deck, 5 - num_cards)
    

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
        self.holiday = []

    def enque_card(self, card: Card, caster: Entity):
        self.exec_queue.append({
            "card": card,
            "owner": caster
        })
        self.exec_queue.sort(key=lambda c: c["card"].card_type.value)

    def execute_card(self, card: Card, caster: Entity):

        print(f"{caster.name} is using {card.card_name}...")

        c_target = card.card_target
        targets: list[Entity] = []

        if (c_target == CardTarget.PLAYERS):
            targets += self.players
        elif (c_target == CardTarget.SELF):
            targets.append(caster)
        elif (c_target == CardTarget.ENEMY):
            targets.append(self.curr_boss)
        elif (c_target == CardTarget.ALL):
            targets += self.all_entities()
        elif (c_target == CardTarget.TARGETTED):
            self.simulator.target_select(card, targets, self)
        
        # Remove any targets currently on a holiday
        targets = list(filter(lambda t: t not in self.holiday, targets))
            

        def calculate_damage(strength, modifier, shield):
            return strength + modifier - shield

        c_type = card.card_type
        c_str = card.card_strength

        for entity in targets:
            if (c_type == CardType.DAMAGE):
                entity.health -= calculate_damage(c_str, entity.modifier, entity.shield)
            elif (c_type == CardType.HEAL):
                entity.health += c_str + entity.modifier
            elif (c_type == CardType.BUFF):
                entity.modifier += c_str
            elif (c_type == CardType.DEBUFF):
                entity.modifier -= c_str
            elif (c_type == CardType.SHIELD):
                entity.shield += c_str

        if card.card_special is not None:
            card.card_special(card, self, caster)

    def execute_queue(self):

        for c in self.exec_queue:
            self.execute_card(c["card"], c["owner"])

        self.exec_queue = []

