import numpy as np 
import random 

#change player postion-shot
def cpps (pm , pp):
    if pm == "d":
        pp[0] += 1
    elif pm == "a":
        pp[0] -= 1
    elif pm == "w":
        pp[1] = 1
    elif pm == "wd" or pm == "dw":
        pp[1] = 1 
        pp[0] += 1
    elif pm == "aw" or pm == "wa":
        pp[1] = 1
        pp[0] -= 1
    elif pm == "w" :
        pp[1] = 1
    return pp

def make_bult (column_of_player , bult_pos):
    bult_pos.append([18,column_of_player])
    return bult_pos

def shoting (bult_pos):
    for i in bult_pos:
        if i[0] > 0 :
            i[0] -= 1
        else:
            bult_pos.remove(i)
    return bult_pos

def make_enemy(eps):
    eps.append([0,random.randint(0,9)])
    return eps
        
def enemy_movments (eps):
    for i in eps:
        if i[0] > 18:
            eps.remove(i)
        else:
            i[0] += 1
    return eps
    
def tbANDe (bult_pos , enemy_pos , score):
    eab = []
    for i in bult_pos:
        for j in enemy_pos:
            if i == j :
                bult_pos.remove(i)
                enemy_pos.remove(j)
                score += 1
    eab.append(bult_pos)
    eab.append(enemy_pos)
    eab.append(score)
    return eab
                





def cheek_range(col):
    win = 0 
    if col > 9 or col < 0 :
        win = 1
    return win 



game_table = np.zeros(200).reshape(20,10)
player_colAshot = [4 , 0]
win = 0 
bult_postions = []
enemies_postion = []
score = 1
s = 1
a = 1
counter = 0
while win == 0 :
    game_table[19][player_colAshot[0]] = 8


    if player_colAshot[1] == 1:
        bult_postions = make_bult(player_colAshot[0] , bult_postions)
        game_table[bult_postions[0][0]][bult_postions[0][1]] = 1
    if counter == 10 :
        if s % 5 == 0 :
            a += 1
            s += 1
        for i in range(a):
            enemies_postion = make_enemy(enemies_postion)
            for i in range(a):
                game_table[enemies_postion[i][0]][enemies_postion[i][1]] = 7
        counter  = 0 
        
    player_colAshot[1] = 0 
    print(f"\n\n\n\n\n\nSCORE : {score}\n\n\n\n\n\n{game_table}\n\n\n")
    game_table[19][player_colAshot[0]] = 0
    move = input()
    player_colAshot= cpps(move,player_colAshot)

    
    enemies_postion = tbANDe(bult_postions , enemies_postion , score)[1]
    bult_postions = tbANDe(bult_postions , enemies_postion , score)[0]
    score += tbANDe(bult_postions , enemies_postion , score)[2]

    b = 0 
    for i in enemies_postion:
        game_table[enemies_postion[b][0]][enemies_postion[b][1]] = 0
        b+= 1
    enemies_postion = enemy_movments(enemies_postion)
    b = 0 
    for i in enemies_postion:
        game_table[enemies_postion[b][0]][enemies_postion[b][1]] = 7
        b += 1
        
    b = 0 
    for i in bult_postions:
        game_table[bult_postions[b][0]][bult_postions[b][1]] = 0 
        b += 1
    bult_postions = shoting(bult_postions)
    b = 0 
    for i in bult_postions:
        game_table[bult_postions[b][0]][bult_postions[b][1]] = 1 
        b += 1

    s += 1
    counter +=1 
    win = cheek_range(player_colAshot[0])
    
    
if win == 1 :
    print("DON'T GO TO THE OUT OF MATRIS")

    
    
    
    
    
    
    
    
