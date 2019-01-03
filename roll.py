import random
def roll_dice (die_roll, dice_parameters):
    num_dice, dice_type, num_faces = dice_parameters
    for y in range(num_dice):
        die_roll.append(random.randint(1, num_faces))
    return (die_roll)
def keep_drop (die_roll, kd_mod):
    kd_mode, kd_num = kd_mod
    num_dice = len(die_roll)
    dice_dropped = []
    dice_kept = []
    die_roll.sort()
    if(kd_num is None):
        kd_mode = 1
    if(kd_mode == "k" and kd_num > 0):
        dice_dropped = die_roll[(num_dice-kd_num):num_dice]
        dice_kept = die_roll[0:(num_dice-kd_num)]
    elif(kd_mode == "d"):
        dice_dropped = die_roll[0:kd_num]
        dice_kept = die_roll[kd_num:num_dice]
    kd_print = " Dice Kept: " + str(dice_kept) + " Dice Dropped: " + str(dice_dropped)
    return(dice_kept, kd_print)
def raise_lower (total, rl_mod):
    rl_str = ""
    rl_mode, rl_val = rl_mod
    if(rl_mode == "r"):
        if(total < rl_val):
            total = rl_val
            rl_str = " Raised to " + str(rl_val)
    elif(rl_mode == "l"):
        if(total > rl_val):
            total = rl_val
            rl_str = " Lowered to " + str(rl_val)
    return(total, rl_str)

roll_in = {         # Dictionary defines roll from parameters passed from parser
'iterations' : 6,   # how many times the rolls happen
'dice_parameters' : ( 4 , 'd' , 6 ),    #(dice per roll, dice type, number of faces on die)
'roll_mod' : 0,  # Any +/- modifier to the roll
'kd_mod' : ( 'd' , 1 ),     # (k)eep or (d)rop high or low; number of dice to keep/drop (can be negative)
'rl_mod' : ( 'r' , 8 ),     # (r)aise or (l)ower total roll if it goes beyond threshol;, threshold value
}

# The default roll will populate any parameters left blank in the parser
default_roll = {    
'iterations' : 1,   
'dice_parameters': (1, 'd', 20),
'roll_mod' : 0,  
'kd_mod' : (None, None),    
'rl_mod' : (None, None)
}          

for key in roll_in:
    if not roll_in[key]:
        roll_in[key] = default_roll[key]

roll_print = []
for x in range(roll_in['iterations']):
    kd_print, sum_print, rl_print = '', '', ''
    die_roll = []
    die_roll = roll_dice(die_roll, roll_in['dice_parameters'])
    if(roll_in['kd_mod'][0]):
        dice_kept, kd_print = keep_drop(die_roll, roll_in['kd_mod'])
    else:
        dice_kept = die_roll
    #sum and roll mod functions     
    sum = 0
    for i in dice_kept:
        sum += i 
        sum += roll_in['roll_mod']
    if(roll_in['rl_mod'][0] and roll_in['rl_mod'][1]):
            sum, rl_print = raise_lower(sum,roll_in['rl_mod'])
    sum_print = "Result: " + str(sum)
    if(roll_in['roll_mod']):
        sum_print = "Result: " +str(sum)+ "  (Modified with " + str(roll_in['roll_mod']) + ")"            
    roll_print.append(sum_print + rl_print + kd_print)
    
    
for x in roll_print:
    print(x)


