class Cell:
    def __init__(self, action_name, border_color, fill_color, action_function):
        self.action_name = action_name
        self.border_color = border_color
        self.fill_color = fill_color
        self.action_function = action_function

    def perform_action(self, game, player):
        if self.action_function:
            self.action_function(game, player)
