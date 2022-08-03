# Write your solution here
def who_won(game_board: list):
    winner_value = 0
    player_one_points = 0
    player_two_points = 0
    for row in game_board:
        for element in row:
            if element == 1:
                player_one_points+=1
            elif element ==2:
                player_two_points+=1
    if player_one_points > player_two_points:
        winner_value = 1
    elif player_two_points > player_one_points:
        winner_value = 2
    return winner_value

