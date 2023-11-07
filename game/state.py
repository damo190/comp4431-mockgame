import random
from enum import Enum
from entities import Player, Boss
from cards.card_list import boss_catalog
from game import Game


class GameState(Enum):
    CHOOSE = 0
    BOSS_CHOOSE = 1
    EXECUTE = 2
    PLAYERS_WON = 3
    BOSS_WON = 4


def boss_choose_stage(game: Game, boss: Boss):
    boss_card = random.choice(list(boss_catalog.keys()))
    game.enque_card(boss_catalog[boss_card], boss)


def check_end_state(game: Game, curr_state: GameState) -> GameState:
    if all(p.health <= 0 for p in game.players):
        return GameState.BOSS_WON
    if game.curr_boss.health <= 0:
        return GameState.PLAYERS_WON
    

    for p in game.players:
        if p.health <= 0:
            print(f"{p.name} is dead!")
    # Remove dead players
    game.players = list(filter(lambda p: p.health > 0, game.players))


    return curr_state

def execute_state(game_state, game: Game):
    if game_state == GameState.CHOOSE:
        for player in game.players:
            game.simulator.choose_stage(player, game)
        game_state = GameState.BOSS_CHOOSE
    
    if game_state == GameState.BOSS_CHOOSE:
        boss_choose_stage(game, game.curr_boss)
        game_state = GameState.EXECUTE
    
    if game_state == GameState.EXECUTE:
        # print("Executing cards...")
        game.execute_queue()
        game.players_draw()
        game_state = GameState.CHOOSE

        game_state = check_end_state(game, game_state)
    return game_state

def play(game: Game):
    state = GameState.CHOOSE
    while state != GameState.BOSS_WON and state != GameState.PLAYERS_WON:
    # while game.turn < game.max_turns and state != GameState.BOSS_WON and state != GameState.PLAYERS_WON:
        print(game)
        state = execute_state(state, game)
        if state == GameState.CHOOSE:
            game.turn += 1

    print("Game Over!")
    print(game)
    if state == GameState.PLAYERS_WON:
        return True
    return
