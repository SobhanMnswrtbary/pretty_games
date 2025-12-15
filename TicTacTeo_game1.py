import numpy as np 


game_table = np.zeros(9).reshape(3,3)


def cheek_win (gt):
    li = []
    winner = 0 
    for i in gt:
        if sum (i) == 12:
            winner = 4 
        elif sum(i) == 9 :
            winner = 3
    
    for i in range(3):
        if sum([ gt[j][i]  for j in range(3)]) == 12:
            winner = 4
        elif sum([ gt[j][i]  for j in range(3)]) == 9:
            winner = 3

    if sum([ gt[i][i] for i in range(3)]) == 12 :
        winner = 4
    elif sum([ gt[i][i] for i in range(3)]) == 9 :
        winner =3

    b = 2 
    l = []
    for i in range(3):
        l.append(gt[i][b])
    if sum(l) == 12:
        winner = 4 
    elif sum(l) == 9 :
        winner = 3

    return winner

win = 0 
print(game_table)
player = int(input("which player do you want to start(3,4) : "))
while player != 3 and player != 4 :
    player = int(input("which player do you want to start(3,4) : "))
if player == 3 :
    s = 1
    e = 10
else:
    s = 2 
    e = 11 


while win == 0 :
    if s !=  e :
        row = int(input("row (0/1/2) : "))
        column = int(input("column (0/1/2) : "))
        if game_table[row][column] == 0 :
            while row > 2 or row < 0 :
                row = int(input("(0/1/2) : "))
            while column > 2 or column < 0 :
                column = int(input("(0/1/2) : "))
            if s % 2 != 0 :
                game_table[row][column] = 3 
            else:
                game_table[row][column] = 4
            s += 1
            win = cheek_win(game_table)
            print(game_table)
        else:
            print("you should select a zero index !")
    else:
        win = 1   

if win == 1 :
    print("Game is over without winner")
elif win == 3 :
    print("player 3 is winner")
elif win == 4:
    print("player 4 is winner")
        


