import random

#roll_in = [iterations, num_dice, game_id, sides_dice, roll_mod, kd_mod, kd_num, rl_mod, rl_num]

iterations = 6
num_dice = 4
game_id = 0
sides_dice = 6 #required
roll_mod = 0
kd_mod = "d"
kd_num = 1
rl_mod = "r"
rl_num = 8

roll_dict = {"iterations" : 6}
roll_print = []
if(not iterations):
    iterations=1
for x in range(iterations):
    die_roll = []
    for x in range(num_dice):
        die_roll.append(random.randint(1, sides_dice))
    
    if(kd_mod):
        dice_dropped = []
        dice_kept = []
        die_roll.sort()
        if ( not kd_num):
            kd_num = 1
        if kd_mod == "k" :
            dice_dropped = die_roll[(num_dice-kd_num):num_dice]
            dice_kept = die_roll[0:(num_dice-kd_num)]
        elif kd_mod == "d" :
            dice_dropped = die_roll[0:kd_num]
            dice_kept = die_roll[kd_num:num_dice]
            
    sum = 0
    for x in dice_kept:
        sum += x
    if(rl_mod and rl_num):
        if(rl_mod == "r"):
            if(sum < rl_num):
                sum = rl_num
        elif(rl_mod == "l"):
            if(sum > rl_num):
                sum = rl_num
    roll_print.append("Result: " + str(sum) + " Dice Kept: " + str(dice_kept) + " Dice Dropped: " + str(dice_dropped))
    
for x in roll_print:
    print(x)

