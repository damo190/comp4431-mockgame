import random
from enum import Enum
from game.exec_que import enque_card, execute_queue
from entities import Card, CardTarget, CardType, Player, Boss
from cards.card_list import boss_catalog

class GameState(Enum):
    CHOOSE = 0
    BOSS_CHOOSE = 1
    EXECUTE = 2
    END = 3



def choose_stage(player: Player, game_stats):
    print("Please select a card numbered above: ", end="")
    # No error checking for now
    choice = int(input())
    chosen_card = player.hand[choice - 1]
    enque_card(chosen_card, "player")
    # execute_card(chosen_card, game_stats, "player")
    del player.hand[choice - 1]

def boss_choose_stage(boss: Boss, game_stats):
    boss_card = random.choice(list(boss_catalog.keys()))
    enque_card(boss_catalog[boss_card], "boss")
    # execute_card(boss_catalog[boss_card], game_stats, "boss")


def check_end_state(game_stats):
    for entity in game_stats:
        if game_stats[entity].health <= 0:
            return True
        
    return False

def execute_state(game_state, game_stats):
    if game_state == GameState.CHOOSE:
        choose_stage(game_stats["player"], game_stats)
        game_state = GameState.BOSS_CHOOSE
    
    if game_state == GameState.BOSS_CHOOSE:
        boss_choose_stage(game_stats["boss"], game_stats)
        game_state = GameState.EXECUTE
    
    if game_state == GameState.EXECUTE:
        # print("Executing cards...")
        execute_queue(game_stats)
        game_state = GameState.CHOOSE

        if check_end_state(game_stats):
            game_state = GameState.END
    return game_state