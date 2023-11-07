from game import Game
from game.state import play
from simulators import manual, rand_brain, power_players
from datetime import datetime

''' 
Alter the test conditions here

Simulator list currently:
    manual - play the game yourself (not recommended for testing balance)
    rand_brain - every move made by both players and bosses is fully random
'''
NUM_PLAYERS = 3
CARDS_IN_HAND = 5
TOTAL_GAMES = 500
SIMULATOR = rand_brain

def manual_play():
    play(Game(2, 5, manual))


def standard_test(debug = False, sim = SIMULATOR):
    win_count = 0
    loss_count = 0
    test_time = datetime.now()

    win_turns = 0
    lose_turns = 0
    total_bosses_beaten = 0

    boss_losses =  {
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }

    f = open("results/results-" + sim.name + "-" + test_time.strftime("%H-%M-%S") + ".txt", 'x')   

    for i in range(TOTAL_GAMES):
        (victory, total_turns, bosses_bested) = play(Game(NUM_PLAYERS, CARDS_IN_HAND, sim))
        total_bosses_beaten += bosses_bested
        if victory:
            win_count += 1
            if debug:
                f.write(f"\tAttempt {i + 1} Won: Beat {bosses_bested} bosses in {total_turns} turns\n")
            win_turns += total_turns
        else:
            if debug:
                f.write(f"\tAttempt {i + 1} Lost: Beat {bosses_bested} bosses in {total_turns} turns\n")
            lose_turns += total_turns
            loss_count += 1
            boss_losses[bosses_bested] += 1
        

    '''
    Write statistics to results file in results/
    '''
    f.write(f"From {TOTAL_GAMES} games, the players won {win_count} times\n")
    f.write(f"Total Winrate: {win_count / TOTAL_GAMES * 100}%\n")
    f.write(f"On average wins took {win_turns / win_count} turns\n")
    f.write(f"On average losses took {lose_turns / loss_count} turns\n")
    f.write(f"The average game lasted {(win_turns + lose_turns) / TOTAL_GAMES} turns\n")
    f.write(f"On average the players bested {total_bosses_beaten / TOTAL_GAMES} bosses\n")
    f.write(f"Boss loss matrix: {boss_losses}\n")

    f.close()

def alter_cards(min_cards, max_cards):
    card_wins = {}
    for cards in range(min_cards, max_cards + 1):
        card_wins[cards] = 0
    for _ in range(TOTAL_GAMES):
        for cards in range(min_cards, max_cards + 1):
            if play(Game(NUM_PLAYERS, cards, SIMULATOR)):
                card_wins[cards] += 1

    test_time = datetime.now()
    with open("results/results-hand-diff-" + test_time.strftime("%H-%M-%S") + ".txt", 'x') as f:
        f.write(f"From {TOTAL_GAMES} games, the different wins based off of card wins are {card_wins}\n")
        for c in card_wins:
            f.write(f"\t{c}: Wins: {card_wins[c]}; Win Rate: {card_wins[c] / TOTAL_GAMES * 100}%\n")

def alter_players(min_players, max_players):
    player_wins = {}
    for players in range(min_players, max_players + 1):
        player_wins[players] = 0
    for _ in range(TOTAL_GAMES):
        for players in range(min_players, max_players + 1):
            if play(Game(players, CARDS_IN_HAND, SIMULATOR)):
                player_wins[players] += 1
    
    test_time = datetime.now()
    with open("results/results-player-diff-" + test_time.strftime("%H-%M-%S") + ".txt", 'x') as f:
        f.write(f"From {TOTAL_GAMES} games, the different wins based off of player wins are: \n")
        for p in player_wins:
            f.write(f"\t{p}: Wins: {player_wins[p]}; Win Rate: {format(player_wins[p] / TOTAL_GAMES * 100, '.2f')}%\n")
    

def main():
    standard_test(True, power_players)
    # standard_test(False, rand_brain)
    # alter_cards(2, 10)
    # alter_players(2, 6)

    # manual_play()
main()