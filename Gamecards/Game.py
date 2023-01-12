from CardGame_Class import CardGame

player1 = input("enter first player's name: ")
player2 = input("enter second player's name: ")
cards = int(input("enter amount of cards for each player to have: "))
# temp player names. will be changed later to both being inputs
# player1 = f'jimmy'
# player2 = f'dudi'
# cards = 26

# set up the game - create deck and shuffle it, then deal cards to the players
war = CardGame(player1, player2, cards)
print(f'The players are {war.player_a.player_name} and {war.player_b.player_name} with {cards} cards each.\n'
      f'the first player is {war.player_a.player_name},his/hers hand is {war.player_a.player_hand}\n'
      f'the second player is {war.player_b.player_name},his/hers hand is {war.player_b.player_hand}\n'
      f'Let the game begin!')

# gets a card from each player's deck
for i in range(10):
    card1 = war.player_a.get_card()
    print(f"{war.player_a.player_name} draws {card1}")
    card2 = war.player_b.get_card()
    print(f"{war.player_b.player_name} draws {card2}")

    # compares between the two cards then prints the winner and adds both cards to his deck
    if card1 > card2:
        war.player_a.add_card(card1)
        war.player_a.add_card(card2)
        print(f"This round's winner is {war.player_a.player_name}!")
    else:
        war.player_b.add_card(card1)
        war.player_b.add_card(card2)
        print(f"This round's winner is {war.player_b.player_name}!")

    # a break between each round, just for the drama
    dramatic_break = input("press enter to continue")

# endgame - declaring the winner
if (len(war.player_a.player_hand)) > len(war.player_b.player_hand):
    print(f"And the winner is..... {war.player_a.player_name}!\n{war.player_a.player_hand}")
elif (len(war.player_a.player_hand)) == len(war.player_b.player_hand):
    print(f"And the winner is...... Nobody!\n"
          f"{war.player_a.player_name} and {war.player_b.player_name} have the same amount of cards.")
else:
    print(f"And the winner is..... {war.player_a.player_name}!\nThe winning hand - {war.player_a.player_hand}")
