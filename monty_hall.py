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

win_count = 0
game_count = 1000000
for _ in range(game_count) :
    if monty_hall_game(True) == 'car' :
        win_count += 1
print(f'win percentage with switch door : {win_count / game_count * 100}')

for _ in range(game_count) :
    if monty_hall_game(False) == 'car' :
        win_count += 1
print(f'win percentage without switch door : {win_count / game_count * 100}')
