from entities import Boss, Card, CardTarget, CardType

class DerangedCow(Boss):

    passive_card = Card(CardType.DAMAGE, 2, CardTarget.PLAYERS, "bloodthirsty_charge", "It's healing while dealing!")

    def passive(self, game):
        self.health = 8
        game.execute_card(self.passive_card, self)

    def __init__(self) -> None:
        super().__init__(8, "deranged_cow")
        self.passive_effect = self.passive