from enum import Enum
import random


# Card type enums
# Ordering changes the order in which cards are execute at the execute phase
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
    ALL = 4
    TARGETTED = 5

class Card:
    card_name = ""
    card_type = CardType.NONE
    card_strength = 0
    card_special = None
    card_target = CardTarget.NONE
    card_flavour = ""

    def __init__(self, c_type, c_strength, c_target, c_name, c_flavour, c_special = None) -> None:
        self.card_type = c_type
        self.card_strength = c_strength
        self.card_target = c_target
        self.card_special = c_special
        self.card_name = c_name
        self.card_flavour = c_flavour

    def mechanical_str(self) -> str:
        ret = ""
        if self.card_type == CardType.SPECIAL:
            ret += "[SPECIAL]"
        if self.card_type == CardType.SHIELD:
            ret += "[SHIELD]"
        if self.card_type == CardType.BUFF:
            ret += "[BUFF]"
        if self.card_type == CardType.DEBUFF:
            ret += "[DEBUFF]"
        if self.card_type == CardType.HEAL:
            ret += "[HEAL]"
        if self.card_type == CardType.DAMAGE:
            ret += "[DAMAGE]"
        ret += " "
        ret += "strength: " + str(self.card_strength)
        ret += "; targetting "
        if self.card_target == CardTarget.ALL:
            ret += "|ALL|"
        if self.card_target == CardTarget.ENEMY:
            ret += "|BOSS|"
        if self.card_target == CardTarget.PLAYERS:
            ret += "|ALL PLAYERS|"
        if self.card_target == CardTarget.SELF:
            ret += "|YOU|"
        if self.card_target == CardTarget.TARGETTED:
            ret += "|CHOOSE|"
        
        return ret

    def __str__(self) -> str:
        return f"{self.card_name}: {self.mechanical_str()}\n\t{self.card_flavour}\n"
    

class Entity:
    def __init__(self, health, name) -> None:
        self.health = health
        self.name = name
        self.modifier = 0
        self.shield = 0
    
class Player(Entity):
    hand = []

    def draw_card(self, card_catalog, num) -> None:
        
        for _ in range(num):
            card = random.choice(list(card_catalog.keys()))
            self.hand.append(card_catalog[card])

    def __init__(self, card_catalog, name, num_cards) -> None:
        super().__init__(10, name)
        self.hand = []
        self.draw_card(card_catalog, num_cards)
    
    def __str__(self) -> str:
        ret = f"{self.name}: you currently have {self.health} HP\n"
        ret += "Your hand contains:\n"
        for (i, card) in enumerate(self.hand):
            ret += f"\t{i + 1}: {card}\n"
        return ret
    
class Boss(Entity):
    def __init__(self) -> None:
        super().__init__(10, "boss")
    
    def __str__(self) -> str:
        ret = f"\nThe Boss {self.name} has {self.health} HP remaining!\n"
        return ret