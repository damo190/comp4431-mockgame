from cards.impl import *
from entities import Card, CardType, CardTarget

card_catalog = {
    "throw_rotten_eggs" : Card(CardType.DAMAGE, 2, CardTarget.ENEMY, "throw_rotten_eggs"),
    "strike" : Card(CardType.DAMAGE, 4, CardTarget.ENEMY, "strike"),
    "stampede" : Card(CardType.DAMAGE, 6, CardTarget.ENEMY, "stampede"),
    "rotten_tomatoes" : Card(CardType.DAMAGE, 2, CardTarget.ALL, "rotten_tomatoes"),
    "hearty_breakfast": Card(CardType.HEAL, 3, CardTarget.SELF, "hearty_breakfast"),
    "feast_for_one": Card(CardType.HEAL, 5, CardTarget.SELF, "feast_for_one"),
    "food_festival": Card(CardType.HEAL, 2, CardTarget.PLAYERS, "food_festival"),
    "cloudy_meatballs": Card(CardType.HEAL, 3, CardTarget.ALL, "cloudy_meatballs"),
    "leftover_scraps": Card(CardType.HEAL, 5, CardTarget.ENEMY, "leftover_scraps"),
    "overgrown_crops": Card(CardType.SHIELD, 1, CardTarget.SELF, "overgrown_crops"),
    "fertilizer": Card(CardType.BUFF, 2, CardTarget.TARGETTED, "fertilizer"),
    "harvest_season": Card(CardType.BUFF, 2, CardTarget.PLAYERS, "harvest_season"),
    "fetch": Card(CardType.SPECIAL, 0, CardTarget.NONE, "fetch", demonic_chant),
    "noahs_ark": Card(CardType.SPECIAL, 0, CardTarget.NONE, "noahs_ark", demonic_chant),
    "reckless_bull": Card(CardType.SPECIAL, 4, CardTarget.ENEMY, "reckless_bull", demonic_chant),
    "merchant_license": Card(CardType.SPECIAL, 0, CardTarget.NONE, "merchant_license", demonic_chant),
}

boss_catalog = {
    # "devestation": Card(CardType.DAMAGE, 5, CardTarget.TARGETTED, "devestation"),
    "stomp": Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "stomp"),
    # "threatening_roar": Card(CardType.DEBUFF, 1, CardTarget.PLAYERS, "threatening_roar"),
    # "withstand": Card(CardType.SHIELD, 2, CardTarget.SELF, "withstand"),

}