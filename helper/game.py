
class Game:

    def __init__(self):
        lst_board = []
        for i in range(6):
            lst_line = []
            for j in range(7):
                lst_line.append(None)
            lst_board.append(lst_line)

        self.board = lst_board
        self.turn = 0
        self.last_move = []
        self.lst_check = []

    def __str__(self):
        """
        just did this to check I did game right or wrong.
        """
        string = ""
        for row in range(6):
            for col in range(7):
                if self.board[row][col] is None:
                    string += '_ '
                else:
                    string += str(self.board[row][col]) + ' '
            string += '\n'

        return string

    def make_move(self, column):
        """
        this func makes move.
        this func puts player number on list.
        """
        if column > 6 or column < 0:
            raise Exception('Illegal move')
        line = 5
        while line + 2:
            if 0 <= line and self.board[line][column] is None:
                self.board[line][column] = self.get_current_player()
                self.last_move.append([line, column])
                break
            line -= 1
        if self.get_winner() is not None:
            raise Exception('Illegal move')

    def check_winner_col(self, row, col, player):
        """
        this function checks the winner of col part.
        """
        check = 0
        while 0 <= col and self.board[row][col] == player:
            col -= 1
        col += 1
        while col <= 6 and self.board[row][col] == player:
            self.lst_check.append([row, col])
            check += 1
            col += 1
        return check

    def check_winner_row(self, row, col, player):
        """
        this function checks the row part of the winner.
        """
        check = 0
        while row <= 5 and self.board[row][col] == player:
            self.lst_check.append([row, col])
            check += 1
            row += 1
        return check

    def check_winner_left_up(self, row, col, player):
        """
        this function checks the left up to right down part of winner.
        """
        check = 0
        while 0 <= row and 0 <= col and self.board[row][col] == player:
            row -= 1
            col -= 1
        row += 1
        col += 1
        while row <= 5 and col <= 6 and self.board[row][col] == player:
            self.lst_check.append([row, col])
            check += 1
            row += 1
            col += 1
        return check

    def check_winner_left_down(self, row, col, player):
        """
        this function checks left down to right up part of the winner.
        """
        check = 0
        while row <= 5 and 0 <= col and self.board[row][col] == player:
            col -= 1
            row += 1
        col += 1
        row -= 1
        while 0 <= row and col <= 6 and self.board[row][col] == player:
            self.lst_check.append([row, col])
            check += 1
            col += 1
            row -= 1
        return check

    def get_winner(self):
        """
        according to 4 functions of above it checks the winner.
        """
        try:
            [row, col] = self.last_move[-1]
            player = self.get_player_at(row, col)
            #   if check is over 4 then win!!!
            if self.check_winner_col(row, col, player) >= 4:
                return player
            if self.check_winner_row(row, col, player) >= 4:
                return player
            if self.turn == 42:
                return 0
            if self.check_winner_left_up(row, col, player) >= 4:
                return player
            if self.check_winner_left_down(row, col, player) >= 4:
                return player
            else:
                return None
        except:
            return None

    def get_player_at(self, row, col):
        """
        If I put parameters row and col then it finds which player is on that coordinate.
        """
        try:
            if self.board[row][col] is None:
                return None
            elif self.board[row][col] == 1:
                return 1
            else:
                return 2
        except:
            raise Exception('Illegal Location')


    def get_current_player(self):
        """
        according to how many turns it had, it thinks who is the current player.
        """
        if self.turn % 2:
            self.turn += 1
            return 2
        self.turn += 1
        return 1

    def get_winner_cordi(self):
        """
        this function finds where the winner is.
        :return: lst of cordi that where the winner is.
        """
        if self.get_winner() is not None:
            lst_reverse = self.lst_check[::-1]
            lst_cordi = lst_reverse[:4]
            return lst_cordi


#
# if __name__ == '__main__':
#     game = Game()
#     while True:
#         print(game)
#         inp = input("input: ")
#         try:
#             game.make_move(int(inp))
#         except:
#             if game.get_winner() is not None:
#                 print(game)
#                 print(game.get_winner())
#                 break
#             print(game.get_winner())
#             print("illegal move")
