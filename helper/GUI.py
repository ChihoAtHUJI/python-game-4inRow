from tkinter import*
from .game import Game
import tkinter.messagebox
from .ai import AI
import time


class GUI:

    def __init__(self, parent):
        """
        This is the construct of GUI.
        """
        # ___________________object___________________
        self.__game = Game()
        self.__ai_1 = AI(self.__game, 1)
        self.__ai_2 = AI(self.__game, 2)
        self.__parent = parent

        #  ___________________photo____________________
        self.__photo_entry = PhotoImage(file='photo entry.png')
        self.__window_play = PhotoImage(file='window.png')

        # ___________________window____________________
        self.main_window_1 = Canvas(self.__parent, width=800, height=700)
        self.main_window_1.pack()
        self.main_window_1.create_image(400, 350, image=self.__photo_entry)

        #  ______________________buttons__________________
        self.__button_exit = Button(self.__parent, text='exit',
                                    command=self.button_destroy_click).place(x=775, y=0)
        self.__button_1player = Button(self.__parent, text='1 player',
                                       command=self.window_ai_vs_player).place(x=280, y=550)
        self.__button_2player = Button(self.__parent, text='2 players',
                                       command=self.play_window).place(x=370, y=550)
        self.__button_com_vs_com= Button(self.__parent, text='com vs com',
                                         command=self.window_ai_vs_ai).place(x=460, y=550)

        # _________________helper_____________
        self.turn = 1
        self.lst_col = [0, 0, 0, 0, 0, 0, 0]
        self.ai = self.__ai_1
        self.window_for_play = None
        self.exit = 0
        self.__parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    #  ____________________method for helping game______________________
    def button_destroy_click(self):
        """
        this is command of destroy application.
        """
        self.exit = 1
        self.__parent.destroy()

    def get_color(self):
        """
        this is the method of getting color
        :return: if it is odd number then return 'red' if it is even number then return 'blue'
        """
        if self.turn % 2:
            self.turn += 1
            self.ai = self.__ai_1
            return 'red'
        self.turn += 1
        self.ai = self.__ai_2
        return 'blue'

    def draw_win(self):
        """
        it find if player wins or not.
        """
        if self.__game.get_winner() is not None:
            lst_cordi = self.__game.get_winner_cordi()
            for cordi in lst_cordi:
                cor_x = 93.5 * cordi[1]
                cor_y = 88 * abs(cordi[0]-5)
                self.window_for_play.create_oval(26 + cor_x, 541 - cor_y, 108 + cor_x, 621 - cor_y, fill='yellow')
            tkinter.messagebox.showinfo('WIN', 'Winner is player %s' % self.__game.get_winner())
            self.message_won()

    def message_won(self):
        """
        if someone wins then get the message box that
        play again or exit.
        """
        message = tkinter.messagebox.askyesno('Thank you for playing.',
                                              'Do you want to play again?')
        if message:
            self.window_for_play.destroy()
            self.main_window(self.__parent)
        else:
            self.button_destroy_click()

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.exit = 1
            self.__parent.destroy()

    #  _____________________game windows____________________________
    def main_window(self, parent):
        """
        this is method for doing again
        """
        self.__game = Game()
        self.main_window_1 = Canvas(parent, width=800, height=700)
        self.main_window_1.pack()
        self.main_window_1.create_image(400, 350, image=self.__photo_entry)

        self.__button_exit = Button(parent, text='exit',
                                    command=self.button_destroy_click).place(x=775, y=0)
        self.__button_1player = Button(parent, text='1 player',
                                       command=self.window_ai_vs_player).place(x=280, y=550)
        self.__button_2player = Button(parent, text='2 players',
                                       command=self.play_window).place(x=370, y=550)
        self.__button_com_vs_com = Button(parent, text='com vs com',
                                          command=self.window_ai_vs_ai).place(x=460, y=550)

        self.__ai_1 = AI(self.__game, 1)
        self.__ai_2 = AI(self.__game, 2)
        self.turn = 1
        self.lst_col = [0, 0, 0, 0, 0, 0, 0]
        self.ai = self.__ai_1
        self.__parent.update()

    def play_window(self):
        """
        This is the new window for playing four in row.
        """
        self.main_window_1.destroy()
        self.window_for_play = Canvas(self.__parent, width=700, height=650)
        self.window_for_play.pack()
        self.window_for_play.create_image(350, 350, image=self.__window_play)
        Button(self.window_for_play, text='exit', command=self.button_destroy_click).place(x= 670, y=0)
        for i in range(1, 8):
            Button(self.window_for_play, text='col' + str(i),
                    command=self.move_player_vs_player(i)).place(x=53+93.5*(i-1), y=65)

    def window_ai_vs_player(self):
        """
        this is the message box that player wants to start first.
        if press yes then go to self.player_vs_ai().
        if press no then go to self.ai_vs_player().
        """
        message = tkinter.messagebox.askyesno('Who is the player 1?',
                                              'Do you want to be the first player?')
        if message:
            self.player_vs_ai()
        else:
            self.ai_vs_player()

    def window_ai_vs_ai(self):
        """
        this is the window for ai_vs_ai
        """
        self.main_window_1.destroy()
        self.window_for_play = Canvas(self.__parent, width=700, height=650)
        self.window_for_play.pack()

        self.window_for_play.create_image(350, 350, image=self.__window_play)
        Button(self.window_for_play, text='exit', command=self.button_destroy_click).place(x=670, y=0)
        # program want to continue until it finds winner.
        while self.__game.get_winner() is None and self.exit == 0:
            self.__parent.update()
            time.sleep(0.5)
            col = self.ai.find_legal_move() + 1
            self.move_player(col)
        self.draw_win()

    def player_vs_ai(self):
        """
        this is the window for player_vs_ai
        """
        self.main_window_1.destroy()
        self.window_for_play = Canvas(self.__parent, width=700, height=650)
        self.window_for_play.pack()
        self.__window_play = PhotoImage(file='window.png')
        self.window_for_play.create_image(350, 350, image=self.__window_play)
        Button(self.window_for_play, text='exit', command=self.button_destroy_click).place(x=670, y=0)
        for i in range(1, 8):
            Button(self.window_for_play, text='col' + str(i), command=self.move_player_vs_ai(i)).place(
                x=53 + 93.5 * (i - 1), y=65)

    def ai_vs_player(self):
        """
        this is the window for ai_vs_player
        """
        self.main_window_1.destroy()
        self.window_for_play = Canvas(self.__parent, width=700, height=650)
        self.window_for_play.pack()
        self.__window_play = PhotoImage(file='window.png')
        self.window_for_play.create_image(350, 350, image=self.__window_play)
        Button(self.window_for_play, text='exit', command=self.button_destroy_click).place(x=670, y=0)
        self.__parent.update()
        col = self.__ai_1.find_legal_move() + 1
        time.sleep(0.5)
        self.move_player(col)
        self.__parent.update()
        for i in range(1, 8):
            Button(self.window_for_play, text='col' + str(i), command=self.move_ai_vs_player(i)).place(
                x=53 + 93.5 * (i - 1), y=65)

    # ____________________game movement__________________________
    def move_player(self, i):
        """
        this is the main function of draw a circle in the play_window.
        """
        try:
            cor_y = 88 * self.lst_col[i - 1]
            cor_x = 93.5 * (i - 1)
            color = self.get_color()
            self.window_for_play.create_oval(26 + cor_x, 541 - cor_y, 108 + cor_x, 621 - cor_y, fill=color)
            self.lst_col[i - 1] += 1
            self.__game.make_move(i - 1)
            self.__parent.update()
        except:
            return

    def move_ai_vs_player(self, i):
        """
        this is the method of ai_vs_player.
        i is the column.
        """
        def move():
            if self.lst_col[i-1] >= 6:
                tkinter.messagebox.showinfo('WRONG', 'Illegal move')
            else:
                self.move_player(i)
                self.draw_win()
                #  when there is the winner then program needs to stop.
                if self.__game.get_winner() is not None:
                    return
                self.__parent.update()
                time.sleep(0.2)
                col = self.__ai_1.find_legal_move() + 1
                self.move_player(col)
                self.draw_win()
        return move

    def move_player_vs_player(self, i):
        """
        this is the method of movement of player vs player.
        """
        def move():
            if self.lst_col[i-1] >= 6:
                tkinter.messagebox.showinfo('WRONG', 'Illegal move')
            else:
                self.move_player(i)
                self.__parent.update()
                self.draw_win()
        return move

    def move_player_vs_ai(self, i):
        """
        this is the method of player vs ai.
        """
        def move():
            if self.lst_col[i-1] >= 6:
                tkinter.messagebox.showinfo('WRONG', 'Illegal move')
            else:
                self.move_player(i)
                self.draw_win()
                if self.__game.get_winner() is not None:
                    return
                self.__parent.update()
                time.sleep(0.2)
                col = self.__ai_2.find_legal_move() + 1
                self.move_player(col)
                self.draw_win()
        return move

