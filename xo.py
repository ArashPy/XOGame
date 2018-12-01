
# By: Arash hatamirad
# Linkedin: ar.hatamirad


class XOGame:

    def __init__(self):
        self.board = [['-', '-', '-'], \
                      ['-', '-', '-'], \
                      ['-', '-', '-']];


        self.turn = 'X';
        self.num_acts = 0;


    def act(self, i, j):

        if i < 0 or i > 2 or j < 0 or j > 2:
            return;

        if self.board[i][j] != '-': return;

        self.board[i][j] = self.turn;

        self.num_acts += 1;


    def change_turn(self):
        self.turn = 'X' if self.turn == 'O' else 'O';


    def __repr__(self):
        s = '';

        for i in range(3):
            for j in range(3):
                s += self.board[i][j] + '\t';

            s += '\n';

        return s;


    def has_winner(self):
        b = self.board;

        return b[0][0] == b[0][1] and b[0][1] == b[0][2] and b[0][2] != '-' or \
               b[1][0] == b[1][1] and b[1][1] == b[1][2] and b[1][2] != '-' or \
               b[2][0] == b[2][1] and b[2][1] == b[2][2] and b[2][2] != '-' or \
               b[0][0] == b[1][0] and b[1][0] == b[2][0] and b[2][0] != '-' or \
               b[0][1] == b[1][1] and b[1][1] == b[2][1] and b[2][1] != '-' or \
               b[0][2] == b[1][2] and b[1][2] == b[2][2] and b[2][2] != '-' or \
               b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[2][2] != '-' or \
               b[2][0] == b[1][1] and b[1][1] == b[0][2] and b[0][2] != '-';


    def is_drawn(self):
        return (not self.has_winner()) and self.num_acts == 9;

from tkinter import *;
from tkinter import messagebox;
import tkinter.font;

tk=Tk();
tk.resizable(False, False);
tk.title('Nougats & Crosses game');
tk['bg'] = 'gray';
tk.geometry('450x520');
k=0;

cell=list();
game = XOGame();

def play(x, y, z):
    if not(game.has_winner() or game.is_drawn()):
        if cell[z].cget('text') =='-' :
            game.act(x, y);
            cell[z].configure(text=game.turn);
        else:
            return;
    if game.has_winner():
        messagebox.showinfo("Game over","The winner is :"+game.turn);
        if game.turn == 'X':
            lbl_score_x.configure(text=str(int(lbl_score_x.cget('text'))+ 1));
        else:
            lbl_score_o.configure(text=str(int(lbl_score_o.cget('text'))+ 1));
        gameover();
    elif game.is_drawn():
        messagebox.showinfo("Game over", " Game drawn!");
        gameover();
    else:
        game.change_turn();
        lbl_result2.configure(text=game.turn);

def gameover():
    game.__init__();
    k = 0;
    for i in range(3):
        for j in range(3):
            cell[k].configure(text='-');
            k += 1;
    lbl_result2.configure(text='X');


def restart():
    gameover();
    lbl_score_o.configure(text='0');
    lbl_score_x.configure(text='0');

frame_top=Frame(tk,relief=SUNKEN,height=68,width=395)
frame_down=Frame(tk,relief=SUNKEN,height=250,width=395)
for i in range(3):
    for j in range(3):
        cell.append(Button(frame_down,text='-',command=lambda x=i,y=j,z=k:play(x,y,z), \
                                padx=1,pady=1,font=('Arial',42),height=1,width=4));
        cell[k].grid(row=i,column=j,padx=3,pady=5);
        k+=1;

lbl1=Label(frame_top,text='X:',font=('Arial',24)).grid(row=1,column=1);
lbl2=Label(frame_top,text='O:',font=('Arial',24)).grid(row=3,column=1);
lbl3=Label(frame_top,text='Scores:',font=('verdana',20)).grid(row=2,column=0);
lbl_score_x=Label(frame_top,text='0',font=('verdana',24));
lbl_score_x.grid(row=1,column=3);
lbl_score_o=Label(frame_top,text='0',font=('verdana',24))
lbl_score_o.grid(row=3,column=3);
lbl_result1=Label(frame_top,text='Turn : ',font=('verdana',20));
lbl_result1.grid(row=2,column=4);
lbl_result2=Label(frame_top,text='X',font=('verdana',24))
lbl_result2.grid(row=2,column=5);
btn_restart=Button(frame_top,text='Restart',font=('verdana',18),command=lambda :restart());
btn_restart.grid(row=2,column=6);

frame_top.pack(padx=3,pady=2,fill=BOTH,expand=1);
frame_down.pack(padx=3,pady=2);
mainloop()



