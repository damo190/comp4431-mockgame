from cards.impl import *
from entities import Card, CardType, CardTarget

deck_numbers = {
    "throw_rotten_eggs" :   6,
    "pitchfork" :           12,
    "stampede" :            4,
    "rotten_tomatoes" :     3,
    "hearty_breakfast" :    4,
    "feast_for_one" :       2,
    "food_festival" :       3,
    "cloudy_meatballs" :    3,
    "leftover_scraps" :     2,
    "overgrown_crops" :     4,
    "fertilizer" :          3,
    "harvest_season" :      2,
    "fetch" :               5,
    "noahs_ark" :           3,
    "reckless_bull" :       4,
    "merchant_license" :    2,
}


card_catalog = {
    "throw_rotten_eggs" : Card(CardType.DAMAGE, 2, CardTarget.ENEMY, "throw_rotten_eggs", "It helps... a bit"),
    "pitchfork" : Card(CardType.DAMAGE, 4, CardTarget.ENEMY, "pitchfork", "A swift strike to the gut!"),
    "stampede" : Card(CardType.DAMAGE, 6, CardTarget.ENEMY, "stampede", "A mighty strike to the beast! Begone!"),
    "rotten_tomatoes" : Card(CardType.DAMAGE, 2, CardTarget.ALL, "rotten_tomatoes", "...Gross..."),
    "hearty_breakfast": Card(CardType.HEAL, 3, CardTarget.TARGETTED, "hearty_breakfast", "A tasty meal"),
    "feast_for_one": Card(CardType.HEAL, 5, CardTarget.TARGETTED, "feast_for_one", "A real tasty time!"),
    "food_festival": Card(CardType.HEAL, 2, CardTarget.PLAYERS, "food_festival", "Festivities all around!"),
    "cloudy_meatballs": Card(CardType.HEAL, 3, CardTarget.ALL, "cloudy_meatballs", "It's raining what?"),
    "leftover_scraps": Card(CardType.HEAL, 5, CardTarget.ENEMY, "leftover_scraps", "You've left out a little treat.."),
    "overgrown_crops": Card(CardType.SHIELD, 1, CardTarget.SELF, "overgrown_crops", "The farm protects!"),
    "fertilizer": Card(CardType.BUFF, 2, CardTarget.TARGETTED, "fertilizer", "Nutritious and delicious"),
    "harvest_season": Card(CardType.BUFF, 2, CardTarget.PLAYERS, "harvest_season", "The best of times"),
    "fetch": Card(CardType.SPECIAL, 0, CardTarget.NONE, "fetch", "Go boy! Fetch!", fetch),
    "noahs_ark": Card(CardType.SPECIAL, 0, CardTarget.NONE, "noahs_ark", "A holy intervention", noahs),
    "reckless_bull": Card(CardType.SPECIAL, 4, CardTarget.ENEMY, "reckless_bull", "No longer in the China shop", reckless_bull),
    "merchant_license": Card(CardType.SPECIAL, 0, CardTarget.NONE, "merchant_license", "Officially Licensed Break", holiday),
}


boss_catalog = {
    # "devestation": Card(CardType.DAMAGE, 5, CardTarget.TARGETTED, "devestation"),
    "stomp": Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "stomp", "rawr stomp!"),
    # "threatening_roar": Card(CardType.DEBUFF, 1, CardTarget.PLAYERS, "threatening_roar"),
    # "withstand": Card(CardType.SHIELD, 2, CardTarget.SELF, "withstand"),

}


def create_deck():
    deck = []
    for card in deck_numbers:
        for _ in range(deck_numbers[card]):
            deck.append(card_catalog[card])

    return deck
    