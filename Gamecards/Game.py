from CardGame_Class import CardGame

# This is the main file the combines the classes and runs as the end user wanted
# it at first takes 2 inputs for the players names in the game
# and then an input for how many cards each player will hold in their hand
player1 = input("enter first player's name: ")
player2 = input("enter second player's name: ")
cards = int(input("enter amount of cards for each player to have: "))

# 2 values to keep track and post the score of the game for easier tracking of the points
player1score = 0
player2score = 0

# Initialization of the game with the inputs from the user
war = CardGame(player1, player2, cards)

# Print out of both the players with both of their respective decks in hand
print(f'The players are {war.player_a.player_name} and {war.player_b.player_name}'
      f' with {len(war.player_a.player_hand)} cards each.\n'
      f'the first player is {war.player_a.player_name},his/hers hand is {war.player_a.player_hand}\n'
      f'the second player is {war.player_b.player_name},his/hers hand is {war.player_b.player_hand}\n'
      f'Let the game begin!')

# There can't be a game if the players have no hand to play with
while len(war.player_a.player_hand) or len(war.player_b.player_hand) != 0:
    # Start of the rounds of the match
    for i in range(10):
        # Prints out at the start of the round both cards that the players drew
        card1 = war.player_a.get_card()
        print(f"{war.player_a.player_name} draws {card1}")
        card2 = war.player_b.get_card()
        print(f"{war.player_b.player_name} draws {card2}")
        # Compares between the 2 drawn cards
        # the player with the highest value card gets both cards added to his hand and a point added to his score
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
        # In case both players play the same card which should be impossible by design an error pops out about cheating
        else:
            if card1 == card2:
                raise ValueError("Someones cheating.")

        # a break between each round, for a cleaner print out of each round but mostly for the added drama and suspense
        print(f'\nThe score is {player1score} points to {war.player_a.player_name}'
              f' and {player2score} points to {war.player_b.player_name}\n')
        dramatic_break = input("press enter to continue\n")
    else:
        break

# Getting the winner after the rounds by the players respective deck on hand size and printing the winner
winner = war.get_winner()
print("And the winner is...")
if winner == war.player_a or winner == war.player_b:
    print(war.get_winner().player_name)
# In case of a draw prints out no winner
else:
    print("No one the games is a draw.")