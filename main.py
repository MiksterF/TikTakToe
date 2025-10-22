from turtle import Screen, Turtle
from tkinter import *
import random
import sys
from itertools import cycle
import time

player1, player2 = ['comp'], ['player2']
list_of_players = [player2, player1]
players = cycle(list_of_players)
current_player = player1
all_marks_on_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tk_window = Tk()

class Field(Turtle):
    def __init__(self, start, stop):
        super().__init__()
        self.start = start
        self.stop = stop
        self.hideturtle()
        self.penup()
        self.goto(self.start[0], self.start[1])
        self.pencolor('black')
        self.pendown()
        self.goto(self.stop[0], self.stop[1])

class Victory_case(Turtle):
    def __init__(self, start, stop):
        super().__init__()
        self.hideturtle()
        self.start = start
        self.stop = stop
        self.penup()
        self.goto(self.start[0], self.start[1])
        self.color('green')
        self.pendown()
        self.goto(self.stop[0], self.stop[1])


    def __srt__(self):
        return f'{self.start}, {self.stop}'

class Turns(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 180)
        self.color('black')

    def write_player(self, player):
        self.write(player, align="center", font=("Courier", 24, "normal"))
        return f'{player}test return'

    def announce_winner(self, text):
        self.clear()
        self.write(text, align="center", font=("Courier", 24, "normal"))

    def clear_title(self):
        self.clear()


class Marks(Turtle):
    def __init__(self, x, y, mark):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(mark, align="center", font=("Courier", 24, "normal"))

title = 'fjkdljfk'
screen = 'fjkdlfj'

def check_winnings(current_player):
    global title, screen
    check_cells = {1: (range(-156, -56), range(-14, 86)),
                   2: (range(-50, 50), range(-14, 86)),
                   3: (range(56, 156), range(-14, 86)),
                   4: (range(-156, -56), range(-120, -20)),
                   5: (range(-50, 50), range(-120, -20)),
                   6: (range(56, 156), range(-120, -20)),
                   7: (range(-156, -56), range(-226, -126)),
                   8: (range(-50, 50), range(-226, -126)),
                   9: (range(56, 156), range(-226, -126))}
    win_cases = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for ind, case in enumerate(win_cases):
        if case[0] in current_player and case[1] in current_player and case[2] in current_player:
            if ind in (0,1,2):
                start = (min(check_cells[case[0]][0]), min(check_cells[case[2]][1])+50)
                stop = (max(check_cells[case[2]][0]), min(check_cells[case[2]][1]) + 50)
                vic_mark = Victory_case(start, stop)
                screen.update()
            elif ind in (3, 4, 5):
                start = (min(check_cells[case[0]][0])+50, max(check_cells[case[0]][1]))
                stop = (min(check_cells[case[0]][0])+50, min(check_cells[case[2]][1]))
                vic_mark = Victory_case(start, stop)
                screen.update()
            elif ind == 6:
                start = (-156, 86)
                stop = (156, -226)
                vic_mark = Victory_case(start, stop)
                screen.update()
            elif ind == 7:
                start = (156, 86)
                stop = (-156, -226)
                vic_mark = Victory_case(start, stop)
                screen.update()

            title.clear_title()
            title.announce_winner(f'winner is {current_player[0]}')
            time.sleep(3)
            sys.exit()
    if len(all_marks_on_board) < 1:
        title.clear_title()
        title.announce_winner('Its a draw')
        time.sleep(3)
        sys.exit()

def put_marks(x, y, comp_cell):
    global current_player
    if current_player == player1:
        sign = 'X'
    elif current_player == player2:
        sign = 'O'
    check_cells = {1: (range(-156, -56), range(-14, 86)),
                   2: (range(-50, 50), range(-14, 86)),
                   3: (range(56, 156), range(-14, 86)),
                   4: (range(-156, -56), range(-120, -20)),
                   5: (range(-50, 50), range(-120, -20)),
                   6: (range(56, 156), range(-120, -20)),
                   7: (range(-156, -56), range(-226, -126)),
                   8: (range(-50, 50), range(-226, -126)),
                   9: (range(56, 156), range(-226, -126))}

    if x:
        for cell, coord in check_cells.items():
            if x in coord[0] and y in coord[1]:
                if cell in all_marks_on_board:
                    current_player.append(cell)
                    mark = Marks(min(coord[0])+50, min(coord[1])+35, sign)
                    return cell
    elif comp_cell:
        current_player.append(comp_cell)
        for cell, coord in check_cells.items():
            if cell == comp_cell:
                mark = Marks(min(coord[0]) + 50, min(coord[1]) + 35, sign)
                return

def create_welcome_window():
    global tk_window, frm
    frm = Frame(tk_window)
    frm.grid()
    tk_window.minsize(300,300)
    tk_window.config(padx=50, pady=50)
    tk_label = Label(frm, text="Welcome to tic tac toe!", font=("Arial", 18, "bold")).grid(column=0, row=0, columnspan=2)
    tk_label2 = Label(frm, text="Please choose: ", font=("Arial", 18, "bold")).grid(column=0, row=1, columnspan=2)
    single_option = Button(frm, text="Single game", command=single_game).grid(column=0, row=2)
    multiplayer_option = Button(frm, text="Multiplayer", command=multiplayer).grid(column=1, row=2)
    frm.mainloop()


def single_game():
    global tk_window, frm
    frm.destroy()
    frm = Frame(tk_window)
    frm.grid()
    tk_window.minsize(300, 300)
    tk_window.config(padx=50, pady=50)
    tk_label = Label(frm, text="Please choose your markings", font=("Arial", 18, "bold")).grid(column=0, row=0, columnspan=2)
    xs = Button(frm, text="Xs", command=lambda: game_started("single", "x")).grid(column=0, row=1)
    os = Button(frm, text="Os", command=lambda: game_started("single", "o")).grid(column=1, row=1)


def multiplayer():
    global player1, player2
    player1[0] = 'player1'
    player2[0] = 'player2'
    game_started('multi', None)


def game_started(mode, mark):
    global tk_window, frm, player1, player2, title, screen
    if mark == 'x':
        player1[0] = 'player1'
        player2[0] = 'comp'
    elif mark == 'x':
        player1[0] = 'comp'
        player2[0] = 'player2'

    tk_window.destroy()
    screen = Screen()
    screen.setup(width=400, height=520)
    screen.tracer(0)

    field1 = Field((-53, -229), (-53, 89)).speed(9)
    field2 = Field((53, -229), (53, 89)).speed(9)
    field3 = Field((-159, -123), (159, -123)).speed(9)
    field4 = Field((-159, -17), (159, -17)).speed(9)
    screen.update()
    title = Turns()


    # i have to add this part because if comp is the first olayer, i dont need to get coord
    if player1[0] == 'comp':
        title.write_player(current_player[0])
        if len(player1) < 2:
            time.sleep(1)
        comp_choice = random.choice(all_marks_on_board)
        all_marks_on_board.remove(int(comp_choice))
        mark = put_marks(None, None, comp_choice)
        check_winnings(current_player)
        switch_players()
        # announce first player
        title.clear_title()
        title.write_player(current_player[0])
    else:
        title.write_player(current_player[0])
    screen.onscreenclick(get_coord)
    screen.mainloop()


def get_coord(x, y):
    global current_player, all_marks_on_board, title
    title.clear_title()
    new_mark = put_marks(x, y, None)
    all_marks_on_board.remove(new_mark)
    check_winnings(current_player)
    switch_players()
    title.write_player(current_player[0])

    if current_player[0] == 'comp':
        time.sleep(1)
        comp_choice = random.choice(all_marks_on_board)
        all_marks_on_board.remove(int(comp_choice))
        mark = put_marks(None, None, comp_choice)
        check_winnings(current_player)
        switch_players()
        title.clear_title()
        title.write_player(current_player[0])

def switch_players():
    global players
    for player in players:
        global current_player
        current_player = player
        return

def main():
    create_welcome_window()

if __name__ == '__main__':
    main()
