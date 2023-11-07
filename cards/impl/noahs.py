from entities import Card, CardTarget, CardType

def noahs(card, game, caster):
    target = []
    game.simulator.target_select(target, game)
    chosen_target = target[0]
    
    for (i, e) in enumerate(game.exec_queue):
        if e['owner'].name == chosen_target.name:
            game.exec_queue[i]['card'] = Card(CardType.NONE, 0, CardTarget.NONE, "cancelled", "you have been cancelled!")

