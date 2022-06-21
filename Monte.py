import random

prizes = ["Goat", "Goat", "Goat"]
doors = ["Door 1", "Door 2", "Door 3"]
prizes[random.randint(0,2)] = "Car"
remainingPrizes = prizes.copy()
remainingDoors = doors.copy()

#Ask the contestent for a door number and validate that it is in the correct range
while True:
    ask = input("Please select between Doors 1, 2 and 3")
    #validate resposne
    try:
        if 0 < int(ask) < 4:
            break
        else:
            print('Your selection was invalid. Please select between 1, 2 and 3')
    except:
        print('Your selection was invalid. Please select between 1, 2 and 3')

#Remove the contestents chosen door and prize from the remaining pools
remainingPrizes.pop(int(ask) -1)
remainingDoors.pop(int(ask) - 1)

#Select a random door from the two remaining doors and check if its a Goat or Car.
randomDoor = random.randint(0,1)
if remainingPrizes[randomDoor] == "Goat":
    while True:
        answer = input('There is a ' + remainingPrizes[randomDoor] + ' behind ' + doors[randomDoor] + ', would you like to swap between your original choice of ' + doors[int(ask)] + ' and the one remaining door? (y/n)')
        if answer == 'y':
            if prizes[int(ask)- 1] == 'Car':
                print('You Lose')
                break
            else:
                print('You Win!')
                break
        elif answer == 'n':
            if prizes[int(ask) -1] == 'Car':
                print('You Win')
                break
            else:
                print('You Lose')
                break
        else:
            print('Your selection was invalid')
else:
    while True:
        answer = input('There is a ' + remainingPrizes[randomDoor - 1] + ' behind ' + remainingDoors[randomDoor - 1] + '. Would you like swap between your orginal choice of ' + doors[int(ask)] + ' and the last remaining door?')

        if answer == 'y':
            if prizes[int(ask)- 1] == 'Car':
                print('You Lose')
                break
            else:
                print('You Win!')
                break
        elif answer == 'n':
            if prizes[int(ask) -1] == 'Car':
                print('You Win')
                break
            else:
                print('You Lose')
                break
        else:
            print('Your selection was invalid')