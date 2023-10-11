from enum import Enum
import random

class CardType(Enum):
    SPECIAL = -1
    NONE = 0
    SHIELD = 1
    BUFF = 2
    DEBUFF = 3
    HEAL = 4
    DAMAGE = 5

class CardTarget(Enum):
    NONE = 0
    SELF = 1
    PLAYERS = 2
    ENEMY = 3
    TARGETTED = 5
    ALL = 4

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
    

class Entity:
    def __init__(self, health) -> None:
        self.health = health
        self.modifier = 0
        self.shield = 0
    
class Player(Entity):
    hand = []
    def __init__(self, card_catalog) -> None:
        super().__init__(10)
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
    
class Boss(Entity):
    def __init__(self) -> None:
        super().__init__(5)
    
    def __str__(self) -> str:
        ret = f"\nThe Boss has {self.health} HP remaining!\n"
        return ret