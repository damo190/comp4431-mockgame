import random
from game.state import execute_state
from entities import Boss, Player
from game.state import GameState
from cards.card_list import card_catalog


def main():
    player1 = Player(card_catalog)
    boss = Boss()

    game_stats = {
        "boss": boss,
        "player": player1,
    }

    turn = 0
    game_state = GameState.CHOOSE
    while turn < 3:
        for e in game_stats:
            print(game_stats[e])

        game_state = execute_state(game_state, game_stats)
        if (game_state == GameState.CHOOSE):
            turn += 1
        
        if (game_state == GameState.END):
            print("Game over!")
            break

    print("Game ended...")
    for e in game_stats:
        print(game_stats[e])   

    return

main()