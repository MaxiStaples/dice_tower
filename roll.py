import random

#roll_in = [iterations, num_dice, game_id, sides_dice, roll_mod, kd_mod, kd_num, rl_mod, rl_num]

iterations = 5   # how many times the rolls happen
num_dice = 4     # number of dice per roll
game_id = 0      # Game identifier (not implemented)
sides_dice = 6   # (required) Number of sides on the die
roll_mod = None  # Any +/- modifier to the roll
kd_mod = "d"     # (k)eep or (d)rop high or low
kd_num = 1       # The number of dice to keep or drop (can be negative) 
rl_mod = "r"     # (r)aise or (l)ower total roll if it goes beyond threshold
rl_num = 8       # The raise/lower threshold

roll_dict = {"iterations" : 6}
roll_print = []
if(iterations is None):
    iterations = 1
for x in range(iterations):
    die_roll = []
    kd_print, sum_print, rl_print = '', '', ''
    for y in range(num_dice):
        die_roll.append(random.randint(1, sides_dice))
    
    if(kd_mod):
        dice_dropped = []
        dice_kept = []
        die_roll.sort()
        if(kd_num is None):
            kd_num = 1
        if(kd_mod == "k" and kd_num > 0):
            dice_dropped = die_roll[(num_dice-kd_num):num_dice]
            dice_kept = die_roll[0:(num_dice-kd_num)]
        elif(kd_mod == "d"):
            dice_dropped = die_roll[0:kd_num]
            dice_kept = die_roll[kd_num:num_dice]
        kd_print = " Dice Kept: " + str(dice_kept) + " Dice Dropped: " + str(dice_dropped)
            
    sum = 0
    for i in dice_kept:
        sum += i
    if(roll_mod):
        sum += roll_mod
    if(rl_mod and rl_num):
        if(rl_mod == "r"):
            if(sum < rl_num):
                sum = rl_num
                rl_print = " Raised to " + str(rl_num)
        elif(rl_mod == "l"):
            if(sum > rl_num):
                sum = rl_num
                rl_print = " Lowered to " + str(rl_num)
    sum_print = "Result: " + str(sum)
    if(roll_mod):
        sum_print = "Result: " +str(sum)+ "  (Modified with " + str(roll_mod) + ")"            
    roll_print.append(sum_print + rl_print + kd_print)
    
    
for x in roll_print:
    print(x)


