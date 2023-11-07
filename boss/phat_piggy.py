from entities import Boss, Card, CardTarget, CardType

class PhatPiggy(Boss):

    passive_card = Card(CardType.DAMAGE, 0, CardTarget.PLAYERS, "mud_roll", "Is it getting...bigger?")

    turn_count = 0

    def passive(self, game):
        self.turn_count += 1
        self.health += 4
        self.passive_card = Card(CardType.DAMAGE, self.turn_count, CardTarget.PLAYERS, "mud_roll", "Is it getting...bigger?")
        game.execute_card(self.passive_card, self)

    def __init__(self) -> None:
        super().__init__(13, "phat_piggy")
        self.passive_effect = self.passive
        self.turn_count = 0