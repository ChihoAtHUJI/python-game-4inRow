import random

class AI:
    """
    Class ai, it picks random.
    """

    def __init__(self, game, player):
        """
        this is the constructor of AI
        """
        self.game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """
        if it returns to lst of -1 then there are no place to put disc.
        """
        ran_lst = [0, 1, 2, 3, 4, 5, 6]
        while ran_lst != [-1, -1, -1, -1, -1, -1, -1]:
            ran_col = random.choice(ran_lst)
            if ran_col == -1:
                pass
            if self.game.get_player_at(0, ran_col) is None:
                return ran_col
            ran_lst[ran_col] = -1
        raise Exception("No possible AI moves")

    def get_last_found_move(self):
        pass