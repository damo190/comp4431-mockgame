from entities import Boss, Card, CardTarget, CardType

class Scarecrow(Boss):

    passive_card = Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "deadly stare", "you feel...intimidated")

    def passive(self, game):
        game.execute_card(self.passive_card, self)

    def __init__(self) -> None:
        super().__init__(10, "scarecrow")
        self.passive_effect = self.passive