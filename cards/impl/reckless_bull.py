from entities import Card, CardType, CardTarget

def reckless_bull(card, game, caster):
    game.execute_card(Card(CardType.DAMAGE, 4, CardTarget.ENEMY, "reckless damage", "boom"), caster)

    for eq in game.exec_queue:
        if eq['owner'] != caster and eq['owner'].name != "boss":
            if eq['card'].card_type != CardType.DAMAGE:
                eq['owner'].health -= 2
                print(f"{eq['owner'].name}'s health is now {eq['owner'].health}")

    pass