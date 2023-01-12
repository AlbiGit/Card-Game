from Gamecards import CardGame_Class
from Gamecards import Player_Class
from Gamecards import Card_Class

player1 = f'jimmy'
player2 = f'dudi'
war = CardGame_Class.CardGame(player1,player2,26)
print(f'players are {player1} and {player2} with 26 cards each')
for i in range(3):
    card1 = war.player_a.get_card()
    card2 = war.player_b.get_card()
    if card1 > card2:
        war.player_a.add_card(card1)
        war.player_a.add_card(card2)
        print(f'winnter is {war.player_a.player_name} and gets {card1} and {card2}')
    else:
        war.player_b.add_card(card1)
        war.player_b.add_card(card2)
        print(f'winnter is {war.player_b.player_name} and gets {card1} and {card2}')