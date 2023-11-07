from entities import Card, CardTarget, CardType, Entity
from game import Game
exec_queue: list[dict] = []


def enque_card(card: Card, caster: Entity):
    exec_queue.append({
        "card": card,
        "owner": caster
    })
    exec_queue.sort(key=lambda c: c["card"].card_type.value)


def execute_card(card: Card, game: Game, caster: Entity):

    print(f"{caster.name} is using {card.card_name}...")

    c_target = card.card_target
    targets: list[Entity] = []

    if (c_target == CardTarget.PLAYERS):
        targets += game.players
    elif (c_target == CardTarget.SELF):
        targets.append(caster)
    elif (c_target == CardTarget.ENEMY):
        targets.append(game.curr_boss)
    elif (c_target == CardTarget.ALL):
        targets += game.all_entities()
    elif (c_target == CardTarget.TARGETTED):
        game.simulator.target_select(targets, game)
        

    def calculate_damage(strength, modifier, shield):
        return strength + modifier - shield

    c_type = card.card_type
    c_str = card.card_strength

    for entity in targets:
        if (c_type == CardType.DAMAGE):
            entity.health -= calculate_damage(c_str, entity.modifier, entity.shield)
        elif (c_type == CardType.HEAL):
            entity.health += c_str + entity.modifier
        elif (c_type == CardType.BUFF):
            entity.modifier += c_str
        elif (c_type == CardType.DEBUFF):
            entity.modifier -= c_str
        elif (c_type == CardType.SHIELD):
            entity.shield += c_str

    if card.card_special is not None:
        card.card_special(card, game_stats)


def execute_queue(game: Game):
    global exec_queue

    for c in exec_queue:
        execute_card(c["card"], game, c["owner"])

    exec_queue = []

    game.turn_reset()
    