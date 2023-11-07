from entities import Player, Card, CardTarget, CardType
from game.game_obj import Game
import random

class Simulator:
    choose_stage = None
    target_select = None
    name = ""
    def __init__(self, choose_func, target_func, name) -> None:
        self.choose_stage = choose_func
        self.target_select = target_func
        self.name = name

def manual_choose_stage(player: Player, game: Game):
    print(player)
    print(f"{player.name}: please select a card numbered above: ", end="")
    # No error checking for now
    choice = int(input())
    chosen_card = player.hand[choice - 1]
    game.enque_card(chosen_card, player)
    del player.hand[choice - 1]


def random_choose_stage(player: Player, game: Game):
    # No error checking for now
    choice = random.randint(1, len(player.hand))
    chosen_card = player.hand[choice - 1]
    print(f"{player.name} Randomly chose:\n {chosen_card}")
    game.enque_card(chosen_card, player)
    del player.hand[choice - 1]

def power_choose_stage(player: Player, game: Game):
    potentials = []
    # If above or at 5 HP play damage cards, otherwise heal
    if player.health >= 5:
        potentials = list(filter(
            lambda c: 
            c.card_type == CardType.DAMAGE and 
            (
                c.card_target == CardTarget.ENEMY or 
                c.card_target == CardTarget.ALL
            )
            , player.hand))
    else:
        potentials = list(filter(
            lambda c: 
            c.card_type == CardType.HEAL and 
            (
                c.card_target == CardTarget.SELF or 
                c.card_target == CardTarget.PLAYERS or
                c.card_target == CardTarget.ALL
            )
            , player.hand))
    
    # If no cards required, play the highest strength card
    if potentials == []:
        potentials = player.hand
        
    potentials.sort(key=lambda c: c.card_strength, reverse=True)
    chosen_card = potentials[0]

    game.enque_card(chosen_card, player)
    player.hand.remove(chosen_card)

def power_select_target(card: Card, targets, game: Game):
    # If we are healing, heal the lowest HP player
    if card.card_type == CardType.HEAL:
        lowest_hp_player = sorted(game.players, key=lambda p: p.health)[0]
        targets.append(lowest_hp_player)
    else:
        targets.append(game.curr_boss)


def manual_select_target(card: Card, targets, game: Game):
    possible_t = game.all_entities()

    print(f"Please choose who to target for {card}: ")

    for (i, entity) in enumerate(possible_t):
        print(f"\t{i + 1}: {entity.name}")
    choice = int(input()) - 1

    targets.append(possible_t[choice])

def random_select_target(card: Card, targets, game: Game):
    possible_t = game.all_entities()

    choice = random.randrange(0, len(possible_t))

    print(f"We chose {possible_t[choice].name}")
    targets.append(possible_t[choice])


manual = Simulator(manual_choose_stage, manual_select_target, "Manual")
rand_brain = Simulator(random_choose_stage, random_select_target, "Random")
power_players = Simulator(power_choose_stage, power_select_target, "Smarter")