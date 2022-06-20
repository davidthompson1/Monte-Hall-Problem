import random

def monte_hall():
    # Create 3 doors and place goats behind each of them
    doors = {'Door1': 'Goat', 'Door2': 'Goat', 'Door3': 'Goat'}
    # replace a goat with a car
    doors['Door' + str(random.randint(1, 3))] = 'Car'
    # clone the doors dictionary
    remainingDoors = doors.copy()
    while True:
        ask = input('Please choose between Door1, Door2 or Door3')
        # Remove chosen door from the list of remaining doors
        if ask == 'Door1':
            break
        elif ask == 'Door2':
            break
        elif ask == 'Door3':
            break
        else:
            print('Your selection is incorrect')
    remainingDoors.pop(ask)
    # Loop through doors to find one with a goat behind it
    for i in remainingDoors:
        if remainingDoors[i] == 'Goat':
            # reveal the goat and ask if the user wants to swap
            swap = input(
                i + ' contains a Goat. Would you like to swap between your current choice and the 1 remaining door?(y/n)')
            while True:
                if swap == 'n':
                    if doors.get(ask) == 'Car':
                        print('You Win')
                    else:
                        print('You Lose')
                    break
                elif swap == 'y':
                    if doors.get(ask) == 'Goat':
                        print('You Win')

                    else:
                        print('You Lose')
                    break
                else:
                    swap = input('Your input is incorrect, please select between y/n')


if __name__ == '__main__':
    monte_hall()