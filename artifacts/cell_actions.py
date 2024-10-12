

def do_nothing(game, player):
    pass

def add_points(game, player, points):
    player['score'] += points

def subtract_points(game, player, points):
    player['score'] = max(0, player['score'] - points)

def give_point_to_other(game, player, other_players, points):
    chosen_player = prompt_player_choice(player, other_players)
    if chosen_player:
        player['score'] -= points
        chosen_player['score'] += points

def reset_points(game, _):
    for player in game.players.values():
        player['score'] = 0

def move_back(game, dice_roll):
    for other_player in game.players.values():
        other_player['position'] = max(0, other_player['position'] - dice_roll)

def choose_path(game, player):
    path_choice = prompt_path_choice()
    if path_choice:
        player['path'] = path_choice
        player['position'] += player['remaining_spaces']


def prompt_player_choice(player, other_players):
    pass

def prompt_path_choice():
    pass
