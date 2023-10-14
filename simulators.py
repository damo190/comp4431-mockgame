from entities import Player
from game.game_obj import Game
from game.exec_que import enque_card
import random

class Simulator:
    choose_stage = None
    target_select = None
    def __init__(self, choose_func, target_func) -> None:
        self.choose_stage = choose_func
        self.target_select = target_func

def manual_choose_stage(player: Player, game: Game):
    print(player)
    print(f"{player.name}: please select a card numbered above: ", end="")
    # No error checking for now
    choice = int(input())
    chosen_card = player.hand[choice - 1]
    enque_card(chosen_card, player)
    del player.hand[choice - 1]


def random_choose_stage(player: Player, game: Game):
    # No error checking for now
    choice = random.randint(1, len(player.hand))
    chosen_card = player.hand[choice - 1]
    print(f"{player.name} Randomly chose:\n {chosen_card}")
    enque_card(chosen_card, player)
    del player.hand[choice - 1]

def manual_select_target(targets, game: Game):
    possible_t = game.all_entities()

    print("Please choose who to target: ")

    for (i, entity) in enumerate(possible_t):
        print(f"\t{i + 1}: {entity.name}")
    choice = int(input()) - 1

    targets.append(possible_t[choice])

def random_select_target(targets, game: Game):
    possible_t = game.all_entities()

    choice = random.randrange(0, len(possible_t))

    print(f"We chose {possible_t[choice].name}")
    targets.append(possible_t[choice])


manual = Simulator(manual_choose_stage, manual_select_target)
rand_brain = Simulator(random_choose_stage, random_select_target)