
# Play another card
def fetch(card, game, caster):
    if len(game.deck) != 0:

        card_to_play = game.deck.pop(0)
        # print(f"We are going to play {card_to_play}")
        game.execute_card(card_to_play, caster)