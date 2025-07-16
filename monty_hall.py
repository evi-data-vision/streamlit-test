import random

def monty_hall_game(switch_choice) :

    monty_hall = ['goat' , 'car' , 'goat']
    random.shuffle(monty_hall)
    #print(monty_hall)

    first_choice = random.choice(range(len(monty_hall)))
    #print(first_choice)

    revealed_doors = [i for i in range(len(monty_hall)) if i != first_choice and monty_hall[i] != 'car']
    #print(revealed_doors)
    revealed_door = random.choice(revealed_doors)
    #print(revealed_door)

    if switch_choice :
        final_choice = [i for i in range(len(monty_hall)) if i != first_choice and i != revealed_door][0]
    else :
        final_choice = first_choice
    #print(final_choice)
    #print(monty_hall[final_choice])
    return monty_hall[final_choice]
def play(game_count) :

    win_count_with_switch = 0
    for _ in range(game_count) :
        if monty_hall_game(True) == 'car' :
            win_count_with_switch += 1
    win_percent_with_switch = win_count_with_switch / game_count * 100
    #print(f'win percentage with switch door : {win_percent_with_switch}')

    win_count_without_switch = 0
    for _ in range(game_count) :
        if monty_hall_game(False) == 'car' :
            win_count_without_switch += 1
    win_percent_without_switch = win_count_without_switch / game_count * 100
    #print(f'win percentage without switch door : {win_percent_without_switch}')

    #return [win_count_with_switch , win_count_without_switch]
    return win_percent_with_switch , win_percent_without_switch

    
