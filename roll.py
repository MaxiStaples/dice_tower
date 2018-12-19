import random

roll_in = {         # Dictionary defines roll from parameters passed from parser
'iterations' : 6,   # how many times the rolls happen
'num_dice' : 4,     # number of dice per roll
'game_id' : 'd',      # Game identifier (not implemented)
'sides_dice' : 6,   # (required) Number of sides on the die
'roll_mod' : 0,  # Any +/- modifier to the roll
'kd_mod' : ( 'd' , 1 ),     # (k)eep or (d)rop high or low; number of dice to keep/drop (can be negative)
'rl_mod' : ( 'r' , 8 ),     # (r)aise or (l)ower total roll if it goes beyond threshol;, threshold value
}

# The default roll will populate any parameters left blank in the parser
default_roll = {    
'iterations' : 1,   
'num_dice' : 1,     
'game_id' : 'd',      
'sides_dice' : 20, 
'roll_mod' : 0,  
'kd_mod' : (None, None),    
'rl_mod' : (None, None)
}          

for key in roll_in:
    if not roll_in[key]:
        roll_in[key] = default_roll[key]


roll_print = []

for x in range(roll_in['iterations']):
    die_roll = []
    kd_print, sum_print, rl_print = '', '', ''
    for y in range(roll_in['num_dice']):
        die_roll.append(random.randint(1, roll_in['sides_dice']))
    
    if(roll_in['kd_mod'][0]):
        dice_dropped = []
        dice_kept = []
        die_roll.sort()
        if(roll_in['kd_mod'][1] is None):
            roll_in['kd_mod'][1] = 1
        if(roll_in['kd_mod'][0] == "k" and roll_in['kd_mod'][1] > 0):
            dice_dropped = die_roll[(roll_in['num_dice']-roll_in['kd_mod'][1]):roll_in['num_dice']]
            dice_kept = die_roll[0:(roll_in['num_dice']-roll_in['kd_mod'][1])]
        elif(roll_in['kd_mod'][0] == "d"):
            dice_dropped = die_roll[0:roll_in['kd_mod'][1]]
            dice_kept = die_roll[roll_in['kd_mod'][1]:roll_in['num_dice']]
        kd_print = " Dice Kept: " + str(dice_kept) + " Dice Dropped: " + str(dice_dropped)
    else:
        dice_kept = die_roll
            
    sum = 0
    for i in dice_kept:
        sum += i 
        sum += roll_in['roll_mod']
    if(roll_in['rl_mod'][0] and roll_in['rl_mod'][1]):
        if(roll_in['rl_mod'][0] == "r"):
            if(sum < roll_in['rl_mod'][1]):
                sum = roll_in['rl_mod'][1]
                rl_print = " Raised to " + str(roll_in['rl_mod'][1])
        elif(roll_in['rl_mod'][0] == "l"):
            if(sum > roll_in['rl_mod'][1]):
                sum = roll_in['rl_mod'][1]
                rl_print = " Lowered to " + str(roll_in['rl_mod'][1])
    sum_print = "Result: " + str(sum)
    if(roll_in['roll_mod']):
        sum_print = "Result: " +str(sum)+ "  (Modified with " + str(roll_in['roll_mod']) + ")"            
    roll_print.append(sum_print + rl_print + kd_print)
    
    
for x in roll_print:
    print(x)


