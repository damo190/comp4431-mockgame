from entities import Boss, Card, CardTarget, CardType

class InnocentLamb(Boss):

    passive_card = Card(CardType.DAMAGE, 100, CardTarget.PLAYERS, "unholy_decimation", "But it looked so innocent!")

    turn_count = 0

    def passive(self, game):
        self.turn_count += 1
        if (self.turn_count == 3):
            game.execute_card(self.passive_card, self)

    def __init__(self) -> None:
        super().__init__(14, "innocent_lamb")
        self.passive_effect = self.passive
        self.turn_count = 0