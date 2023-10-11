from entities import Card, CardTarget, CardType
exec_queue = []


def enque_card(card: Card, caster: str):
    exec_queue.append({
        "card": card,
        "owner": caster
    })
    exec_queue.sort(key=lambda c: c["card"].card_type.value)

def select_target(targets, game_stats):
    print("Please choose who to target: ")
    for (i, entity) in enumerate(game_stats):
        print(f"\t{i + 1}: {entity}")
    choice = int(input()) - 1
    targets.append(list(game_stats.keys())[choice])

def execute_card(card: Card, game_stats, caster):

    print(f"{caster} is using {card.card_name}...")

    c_target = card.card_target
    targets = []
    if (c_target == CardTarget.PLAYERS):
        targets.append("player")
    elif (c_target == CardTarget.SELF):
        targets.append(caster)
    elif (c_target == CardTarget.ENEMY):
        targets.append("boss")
    elif (c_target == CardTarget.ALL):
        for e in game_stats:
            targets.append(e)
    elif (c_target == CardTarget.TARGETTED):
        select_target(targets, game_stats)
        

    def calculate_damage(strength, modifier, shield):
        return strength + modifier - shield

    c_type = card.card_type
    c_str = card.card_strength

    for t in targets:
        entity = game_stats[t]
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
        card.card_special()


def execute_queue(game_stats):
    global exec_queue
    for c in exec_queue:
        execute_card(c["card"], game_stats, c["owner"])

    exec_queue = []

    for e in game_stats:
        game_stats[e].modifier = 0
        game_stats[e].shield = 0
    