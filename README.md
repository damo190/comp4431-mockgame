<h1>Epic card game simulator</h1>
Run the following to play:

> python main.py

Game runs for 3 turns which can be expanded by changing the while loop in main()


<h2>Modules</h2>

 - cards
   - impl: Place implementation of various special cards here
   - [card_list.py](cards/card_list.py): Add cards to the catalog here
     - card_catalog: list of player cards
     - boss_catalog: list of boss cards
 - game
   - [exec_que.py](game/exec_que.py): Logic of how the cards are execute during the execute stage
   - [state.py](game/state.py): Defines the game state of the game
     - CHOOSE: Each player silently chooses their card to play
     - BOSS_CHOOSE: The boss chooses a card from their deck at random
     - EXECUTE: The cards are execute via the defined order found in exec_que
 - [entities.py](entities.py)
   - Various definitions of the objects type of the games and various enums
   - CardType enum ordering is important, as that is how the execution queue orders
 - [main.py](main.py)
   - main file where the game starts

