from cards.impl import *
from entities import Card, CardType, CardTarget

card_catalog = {
    "strike" : Card(CardType.DAMAGE, 2, CardTarget.ENEMY, "strike", "Lash out at the enemy, striking true!"),
    "holy_strike" : Card(CardType.DAMAGE, 4, CardTarget.ENEMY, "holy_strike", "Channel the gods to smite the opponent"),
    "dangeroues_concoction" : Card(CardType.DAMAGE, 4, CardTarget.ALL, "dangeroues_concoction", "Attempt science, damaging all with your latest invention"),
    "bandages": Card(CardType.HEAL, 3, CardTarget.SELF, "bandages", "Demonstrate your crude medicine skills to heal yourself"),
    "holy_prayer": Card(CardType.HEAL, 2, CardTarget.PLAYERS, "holy_prayer", "Pray to the gods above for medical intervention"),
    "demonic_chant": Card(CardType.HEAL, 4, CardTarget.ALL, "demonic_chant", "Pray to a demonic being, healing all in an eerie fashion...", demonic_chant),
}

boss_catalog = {
    "devestation": Card(CardType.DAMAGE, 5, CardTarget.TARGETTED, "devestation", "Destroy that fool!"),
    "stomp": Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "stomp", "Destroy all those fools!"),
    "threatening_roar": Card(CardType.DEBUFF, 1, CardTarget.PLAYERS, "threatening_roar", "Strike fear into their hearts!"),
    "withstand": Card(CardType.SHIELD, 2, CardTarget.SELF, "withstand", "Hold your ground"),

}