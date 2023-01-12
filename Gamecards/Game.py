from CardGame_Class import CardGame

player1 = input("enter first player's name: ")
player2 = input("enter second player's name: ")
cards = int(input("enter amount of cards for each player to have: "))
player1score = 0
player2score = 0
# temp player names. will be changed later to both being inputs
# player1 = f'jimmy'
# player2 = f'dudi'
# cards = 12
# set up the game - create deck and shuffle it, then deal cards to the players
war = CardGame(player1, player2, cards)
print(f'The players are {war.player_a.player_name} and {war.player_b.player_name}'
      f' with {len(war.player_a.player_hand)} cards each.\n'
      f'the first player is {war.player_a.player_name},his/hers hand is {war.player_a.player_hand}\n'
      f'the second player is {war.player_b.player_name},his/hers hand is {war.player_b.player_hand}\n'
      f'Let the game begin!')

# gets a card from each player's deck
for i in range(10):
    # checks if one of the players has no cards
    if len(war.player_a.player_hand) == 0 or len(war.player_b.player_hand) == 0:
        break
    else:
        card1 = war.player_a.get_card()
        print(f"{war.player_a.player_name} draws {card1}")
        card2 = war.player_b.get_card()
        print(f"{war.player_b.player_name} draws {card2}")

    # compares between the two cards then prints the winner of this round and adds both cards to his deck
    if card1 > card2:
        war.player_a.add_card(card1)
        war.player_a.add_card(card2)
        print(f"This round's winner is {war.player_a.player_name}!")
        player1score += 1
    elif card1 < card2:
        war.player_b.add_card(card1)
        war.player_b.add_card(card2)
        print(f"This round's winner is {war.player_b.player_name}!")
        player2score += 1
    else:
        if card1 == card2:
            raise ValueError("Someones cheating.")

    # a break between each round, just for the drama
    print(f'\nThe score is {player1score} points to {war.player_a.player_name}'
          f' and {player2score} points to {war.player_a.player_name}\n')
    dramatic_break = input("press enter to continue\n")

#checking score and announcing winner of the match
if player1score > player2score:
    print(player1, "wins!")
elif player1score < player2score:
    print(player2, "wins!")
else:
    print('Game ended with a draw!')
# endgame - declaring the winner
# if (len(war.player_a.player_hand)) > len(war.player_b.player_hand):
#     print(f"And the winner is..... {war.player_a.player_name}!\n{war.player_a.player_hand}")
# elif (len(war.player_a.player_hand)) == len(war.player_b.player_hand):
#     print(f"And the winner is...... Nobody!\n"
#           f"{war.player_a.player_name} and {war.player_b.player_name} have the same amount of cards.")
# else:
#     print(f"And the winner is..... {war.player_a.player_name}!\nThe winning hand - {war.player_a.player_hand}")
