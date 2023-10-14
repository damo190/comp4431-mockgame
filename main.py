from game import Game
from game.state import play
from simulators import manual, rand_brain
from datetime import datetime

''' 
Alter the test conditions here

Simulator list currently:
    manual - play the game yourself (not recommended for testing balance)
    rand_brain - every move made by both players and bosses is fully random
'''
NUM_PLAYERS = 4
CARDS_IN_HAND = 3
TOTAL_GAMES = 500
SIMULATOR = rand_brain


def standard_test():
    win_count = 0
    for _ in range(TOTAL_GAMES):
        if play(Game(NUM_PLAYERS, CARDS_IN_HAND, SIMULATOR)):
            win_count += 1

    '''
    Write statistics to results file in results/
    '''
    test_time = datetime.now()
    with open("results/results-" + test_time.strftime("%H-%M-%S") + ".txt", 'x') as f:
        f.write(f"From {TOTAL_GAMES} games, the players won {win_count} times\n")
        f.write(f"Total Winrate: {win_count / TOTAL_GAMES * 100}%")

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
    standard_test()
    alter_cards(2, 10)
    alter_players(2, 6)
main()