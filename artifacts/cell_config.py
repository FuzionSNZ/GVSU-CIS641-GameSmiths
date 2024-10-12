from cell_actions import *
from game_objects import Cell

CELL_TYPES = {
    "Blank": Cell("Blank", "black", "gray", do_nothing),
    "+1": Cell("+1", "black", "green", lambda game, player: add_points(game, player, 1)),
    "+2": Cell("+2", "black", "green", lambda game, player: add_points(game, player, 2)),
    "+3": Cell("+3", "black", "green", lambda game, player: add_points(game, player, 3)),
    "-1": Cell("-1", "black", "red", lambda game, player: subtract_points(game, player, 1)),
    "-2": Cell("-2", "black", "red", lambda game, player: subtract_points(game, player, 2)),
    "-3": Cell("-3", "black", "red", lambda game, player: subtract_points(game, player, 3)),
    "GP": Cell("GP", "black", "pink", lambda game, player: give_point_to_other(game, player, game.other_players(player), 1)),
    "G2": Cell("G2", "black", "white", lambda game, player: give_point_to_other(game, player, game.other_players(player), 2)),
    "TP": Cell("TP", "black", "brown", lambda game, player: give_point_to_other(game, player, game.other_players(player), 1)),
    "T2": Cell("T2", "black", "cyan", lambda game, player: give_point_to_other(game, player, game.other_players(player), 2)),
    "S": Cell("Safe", "black", "blue", do_nothing),
    "N": Cell("N", "black", "yellow", reset_points),
    "Z": Cell("Z", "black", "purple", lambda game, player: move_back(game, game.last_dice_roll)),
    "ChoosePath": Cell("Choose Path", "black", "orange", choose_path),
}
