from cards.impl import *
from entities import Card, CardType, CardTarget

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