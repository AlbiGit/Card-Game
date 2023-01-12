from Gamecards import CardGame_Class
from Gamecards import Player_Class
from Gamecards import Card_Class
from Gamecards import DeckOfCards_Class
"""temp player names will be changed later to both being inputs"""
player1 = f'jimmy'
player2 = f'dudi'
"""number of cards in the game now its set to a static 26"""
cards = 26
"""setup the game"""
war = CardGame_Class.CardGame(player1,player2,cards)
"""deal every player the number of cards needed to play"""
print(f'players are {player1} and {player2} with 26 cards each')
"""start of rounds now static 3 for testing later will change to 10 as needed in the requirement"""
"""gets a card from each players deck and compares them then prints the winner and addes both cards to his deck"""
for i in range(3):
    card1 = war.player_a.get_card()
    card2 = war.player_b.get_card()
    print(card1)
    print(card2)
    if card1 > card2:
        war.player_a.add_card(card1)
        war.player_a.add_card(card2)
        print(f'winnter is {war.player_a.player_name} and gets {card1} and {card2}')
    else:
        war.player_b.add_card(card1)
        war.player_b.add_card(card2)
        print(f'winner is {war.player_b.player_name} and gets {card1} and {card2}')