import numpy as np 
import random 
import time

def enemy_movement(player_pos , enemy_pos):
    c = 0 
    for i in enemy_pos:
        if np.array(player_pos-i)[0] > 0 and np.array(player_pos-i)[1] == 0 :
            enemy_pos[c][0] += 1
        elif np.array(player_pos-i)[0] < 0 and np.array(player_pos-i)[1] == 0:
            enemy_pos[c][0] -= 1
        elif np.array(player_pos-i)[0] == 0 and np.array(player_pos-i)[1] > 0 :
            enemy_pos[c][1] += 1
        elif np.array(player_pos-i)[0] == 0 and np.array(player_pos)[1] < 0:
            enemy_pos[c][1] -= 1


        elif np.array(player_pos-i)[0] > 0 and np.array(player_pos-i)[1] > 0:
            a = random.random()
            if a > 0.5 :
                enemy_pos[c][0] += 1
            else:
                enemy_pos[c][1] += 1
        elif np.array(player_pos-i)[0] > 0 and np.array(player_pos - i)[0] < 0 :
            a = random.random()
            if a > 0.5 :
                enemy_pos[c][0] += 1
            else:
                enemy_pos[c][1] -= 1
        elif np.array(player_pos-i)[0] < 0 and np.array(player_pos-i)[1] < 0 :
            a = random.random()
            if a > 0.5:
                enemy_pos[c][0] -= 1
            else:
                enemy_pos[c][1] -= 1
        elif np.array(player_pos-i)[0] < 0 and np.array(player_pos-i)[1] > 0 :
            a = random.random()
            if a > 0.5 :
                enemy_pos[c][0] -= 1
            else:
                enemy_pos[c][1] += 1
        c += 1
    return enemy_pos

def cheek_play_range(r,c):
    l = False
    if r > 19 :
        l = True
    elif r < 0 : 
        l = True
    elif c > 19:
        l = True
    elif  c < 0 :
        l = True
    return l

def make_food(gt , hm):
    for i in range(hm):
        gt[random.randint(0,19)][random.randint(0,19)] = 5
    return gt

def player_move (pm , pp):
    if pm == "s":
        pp[0] += 1
    elif pm == "w":
        pp[0] -= 1
    elif pm == "d":
        pp[1] += 1
    elif pm == "a":
        pp[1] -= 1
    return pp
game_table = np.zeros(400).reshape(20,20)

game_table = make_food(game_table,10)
enemies_pos = []
for i in range(4):
    r = random.randint(0,19)
    c = random.randint(0,19)
    game_table[r][c] = 7 
    enemies_pos.append([r,c])



player_pos = [9,9]
game_table[player_pos[0]][player_pos[1]] = 1
score = 1
win = 0 
s = 0 
while win == 0 :
    time1 = time.time()
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSCORE : {score}\n\n\n{game_table}\n\n")
    move = input()
    time2 = time.time()
    if game_table[player_pos[0]][player_pos[1]] == 7 :
        win = 2
    if time2 - time1 < 2 :
        game_table[player_pos[0]][player_pos[1]] = 0 
        player_pos = player_move(move , player_pos)
        if cheek_play_range(player_pos[0] , player_pos[1]) == True:
            win = 1
        else:
            if game_table[player_pos[0]][player_pos[1]] == 5 :
                score += 1
                s += 1
                game_table[player_pos[0]][player_pos[1]] = 1
            else:
                game_table[player_pos[0]][player_pos[1]] = 1   
            for i in enemies_pos:
                    r = i[0]
                    c = i[1]
                    game_table[r][c] = 0
            
        
            enemies_pos = enemy_movement(np.array(player_pos) , np.array(enemies_pos))
            c = 0 
            for i in range(3):
                game_table[enemies_pos[c][0]][enemies_pos[c][1]] = 7
                c+= 1

    
    if s == 10 :
        game_table = make_food(game_table,6)
        s = 0 


            

if win == 1 :
    print("YOU SHOULD BE IN WORLD'S GAME")
elif win == 2 :
    print("YOU ARE SO SLOW")

    