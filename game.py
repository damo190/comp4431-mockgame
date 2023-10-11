from enum import Enum
import random

game_states = ["CHOOSE", "BOSS_CHOOSE", "EXECUTE"]

class CardType(Enum):
    NONE = 0
    DAMAGE = 1
    HEAL = 2
    BUFF = 3
    DEBUFF = 4
    SHIELD = 5
    SPECIAL = 6

class CardTarget(Enum):
    NONE = 0
    SELF = 1
    PLAYERS = 2
    ENEMY = 3
    TARGETTED = 5
    ALL = 4

def demonic_chant():
    print("Unholy prayers echo around...")

class Card:
    card_name = ""
    card_type = CardType.NONE
    card_strength = 0
    card_special = None
    card_target = CardTarget.NONE

    def __init__(self, c_type, c_strength, c_target, c_name, c_special = None) -> None:
        self.card_type = c_type
        self.card_strength = c_strength
        self.card_target = c_target
        self.card_special = c_special
        self.card_name = c_name

    def __str__(self) -> str:
        return f"{self.card_name}"

card_catalog = {
    "strike" : Card(CardType.DAMAGE, 2, CardTarget.ENEMY, "strike"),
    "holy_strike" : Card(CardType.DAMAGE, 4, CardTarget.ENEMY, "holy_strike"),
    "dangeroues_concoction" : Card(CardType.DAMAGE, 4, CardTarget.ALL, "dangeroues_concoction"),
    "bandages": Card(CardType.HEAL, 3, CardTarget.SELF, "bandages"),
    "holy_prayer": Card(CardType.HEAL, 2, CardTarget.PLAYERS, "holy_prayer"),
    "demonic_chant": Card(CardType.HEAL, 4, CardTarget.ALL, "demonic_chant", demonic_chant),
}

boss_catalog = {
    "devestation": Card(CardType.DAMAGE, 5, CardTarget.TARGETTED, "devestation"),
    "stomp": Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "stomp"),
    "threatening_roar": Card(CardType.DEBUFF, 1, CardTarget.PLAYERS, "threatening_roar"),
    "withstand": Card(CardType.SHIELD, 2, CardTarget.SELF, "withstand"),

}

class Player:
    hand = []
    health = 10
    modifier = 0
    shield = 0
    def __init__(self) -> None:
        self.health = 10
        self.modifier = 0
        self.shield = 0
        print("The player hand is: ")
        for i in range(3):
            card = random.choice(list(card_catalog.keys()))
            self.hand.append(card_catalog[card])
    
    def __str__(self) -> str:
        ret = f"You currently have {self.health} HP\n"
        ret += "Your hand contains:\n"
        for (i, card) in enumerate(self.hand):
            ret += f"\t{i + 1}: {card}\n"
        return ret

def execute_card(card: Card, game_stats, caster):

    print(f"{caster} is using {card.card_name}...")

    c_target = card.card_target
    targets = []
    if (c_target == CardTarget.PLAYERS):
        targets.append("player")
    elif (c_target == CardTarget.SELF):
        targets.append(caster)
    elif (c_target == CardTarget.ENEMY):
        targets.append("boss")
    elif (c_target == CardTarget.ALL):
        for e in game_stats:
            targets.append(e)
    elif (c_target == CardTarget.TARGETTED):
        print("Please choose who to target: ")
        for (i, entity) in enumerate(game_stats):
            print(f"\t{i + 1}: {entity}")
        choice = int(input()) - 1
        targets.append(list(game_stats.keys())[choice])

    c_type = card.card_type
    c_str = card.card_strength
    if (c_type == CardType.DAMAGE):
        for t in targets:
            game_stats[t].health -= c_str
    elif (c_type == CardType.HEAL):
        for t in targets:
            game_stats[t].health += c_str
    elif (c_type == CardType.BUFF):
        for t in targets:
            game_stats[t].modifier += c_str
    elif (c_type == CardType.DEBUFF):
        for t in targets:
            game_stats[t].modifier -= c_str
    elif (c_type == CardType.SHIELD):
        for t in targets:
            game_stats[t].shield += c_str

    if card.card_special is not None:
        card.card_special()
    


class Boss:
    health = 20
    shield = 0
    modifier = 0
    def __init__(self) -> None:
        self.health = 20
        self.shield = 0
        self.modifier = 0
    
    def __str__(self) -> str:
        ret = f"\nThe Boss has {self.health} HP remaining!\n"
        return ret

def choose_stage(player: Player, game_stats):
    print("Please select a card numbered above: ", end="")
    # No error checking for now
    choice = int(input())
    chosen_card = player.hand[choice - 1]
    execute_card(chosen_card, game_stats, "player")
    del player.hand[choice - 1]

def boss_choose_stage(boss: Boss, game_stats):
    boss_card = random.choice(list(boss_catalog.keys()))
    execute_card(boss_catalog[boss_card], game_stats, "boss")


def main():
    player1 = Player()
    boss = Boss()

    game_stats = {
        "boss": boss,
        "player": player1,
    }


    turn = 0
    game_state = game_states[0]
    while turn < 3:
        for e in game_stats:
            print(game_stats[e])

        if game_state == "CHOOSE":
            choose_stage(player1, game_stats)
            game_state = "BOSS_CHOOSE"
        
        if game_state == "BOSS_CHOOSE":
            boss_choose_stage(boss, game_stats)
            game_state = "EXECUTE"
        
        if game_state == "EXECUTE":
            print("Executing cards...")
            turn += 1
            game_state = "CHOOSE"

    print("Game ended...")
    for e in game_stats:
        print(game_stats[e])   




    return

main()