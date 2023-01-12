from Gamecards import CardGame_Class
from Gamecards import Player_Class
from Gamecards import Card_Class

player1 = f'jimmy'
player2 = f'dudi'
war = CardGame_Class.CardGame(player1,player2,26)
print(f'players are {player1},{player2} with 26 cards each')
for i in range(3):
    card1 = Player_Class.Player.player1.get_card()
    card2 = Player_Class.Player.player2.get_card()
    if card1 > card2:
        player1.Player_Class.Player.add_card(card1)
        player1.Player_Class.Player.add_card(card2)
        print(player1,f'wins and get {card1} and {card2}')
    else:
        player2.Player_Class.Player.add_card(card1)
        player2.Player_Class.Player.add_card(card2)
        print(player2, f'wins and get {card1} and {card2}')
