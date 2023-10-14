import random
from enum import Enum
from game.exec_que import enque_card, execute_queue
from entities import Player, Boss
from cards.card_list import boss_catalog
from game import Game


class GameState(Enum):
    CHOOSE = 0
    BOSS_CHOOSE = 1
    EXECUTE = 2
    END = 3



def choose_stage(player: Player, game: Game):
    print(player)
    print(f"{player.name}: please select a card numbered above: ", end="")
    # No error checking for now
    choice = int(input())
    chosen_card = player.hand[choice - 1]
    enque_card(chosen_card, player)
    # execute_card(chosen_card, game_stats, "player")
    del player.hand[choice - 1]

def boss_choose_stage(boss: Boss):
    boss_card = random.choice(list(boss_catalog.keys()))
    enque_card(boss_catalog[boss_card], boss)


def check_end_state(game: Game):
    if all(p.health <= 0 for p in game.players):
        return True
    if game.curr_boss.health <= 0:
        return True    
    return False

def execute_state(game_state, game: Game):
    if game_state == GameState.CHOOSE:
        for player in game.players:
            choose_stage(player, game)
        game_state = GameState.BOSS_CHOOSE
    
    if game_state == GameState.BOSS_CHOOSE:
        boss_choose_stage(game.curr_boss)
        game_state = GameState.EXECUTE
    
    if game_state == GameState.EXECUTE:
        # print("Executing cards...")
        execute_queue(game)
        game_state = GameState.CHOOSE

        if check_end_state(game):
            game_state = GameState.END
    return game_state

def play(game: Game):
    state = GameState.CHOOSE
    while game.turn < game.max_turns and state != GameState.END:
        print(game)
        state = execute_state(state, game)
        if state == GameState.CHOOSE:
            game.turn += 1

    print("Game Over!")
    print(game)