# PROJECTILE MOTION SIMULATOR
# This program has a built-in menu to help navigate and change values easier
# Enter the letter in the parentheses to access that function, such as typing i for (i)nput
# Output is expected as text for displaying values/other menus or visual for simulating projectiles


import turtle as t
import math as m


def simulate(c):
    # asks to simulate projectile or return to main menu
    while True:
        yn = input('\ndo you want to simulate this projectile? (y/n): ')
        if yn == 'y':
            break

        elif yn == 'n':
            print('returning to main menu...')
            main()
            break

        else:
            print(err)
            continue

    # setting simulation screen and variables,
    screen = t.getscreen()
    screen.screensize(10000, 10000)
    t.clear()
    t.speed(0)
    t.penup()
    vx = m.cos(m.radians(p["angle"][c])) * p["velocity"][c]
    vy = m.sin(m.radians(p["angle"][c])) * p["velocity"][c]
    sh = p["starting height"][c]
    gr = p["ground level"][c]
    g = p['gravity'][c]
    tm = p['timeframe'][c]
    t.goto(0, sh)
    sec = 0

    print('\ndisplaying positions (x, y, time) every 0.1 seconds:')
    while True:
        # updates projectile position using the physics equation for projectile motion
        r = vx * sec
        h = 0.5 * -g * sec ** 2 + vy * sec + sh
        t.pendown()
        t.goto(r, h)
        print(round(r, 2), round(h, 2), round(sec, 2))
        sec = sec + 0.1

        # stops the simulation once projectile reaches ground or reaches specified timeframe
        if round(sec - 0.1, 2) == tm:
            print('timeframe reached!')
            print('returning to main menu...')
            main()
            break

        if h < gr:
            print("projectile has impacted ground!")
            print('returning to main menu...')
            main()
            break


def display(c, a):
    # displaying values and iteration inspired by
    # https://stackoverflow.com/questions/69753918/how-to-print-the-data-with-equal-spacing

    # sets up a neat list to display projectile values
    sep = '-' * 50
    print('here are the values for specified projectile to be', a, ':')
    print('\nVariable', 'Value'.rjust(16))
    print(sep)

    # runs a for loop for every key/value pair in projectile dict and optional simulation
    for k, v in p.items():
        print(k, ':', str(v[c]).rjust(10 + (10 - len(k))))


def edit(c):
    n = '\nnew value added!'

    # choosing menu for which value to edit
    while True:
        try:
            echoice = input(
                '\nedit (g)ravity (v)elocity (a)gnle (s)tarting height (gr)ound level, (t)imeframe, or (e)xit, (d)isplay : ')

            # each editable value
            if echoice == 'g':
                new = float(input('\nenter a new value for gravity: '))
                p['gravity'][c] = new
                print(n)

            elif echoice == 'v':
                new = float(input('\nenter a new value for velocity: '))
                p['velocity'][c] = new
                print(n)

            elif echoice == 'a':
                new = float(input('\nenter a new value for angle: '))
                p['angle'][c] = new
                print(n)

            elif echoice == 's':
                new = float(input('\nenter a new value for starting height: '))
                p['starting height'][c] = new
                print(n)

            elif echoice == 'gr':
                new = float(input('\nenter a new value for ground level: '))
                p['ground level'][c] = new
                print(n)

            elif echoice == 't':
                new = float(input('\nenter a new value for timeframe: '))
                p['timeframe'][c] = new
                print(n)

            elif echoice == 'd':
                display(c, 'displayed')

            elif echoice == 'e':
                print('\nexiting...')
                break

            # error handling
            else:
                print(err)
                continue

        except ValueError:
            print(err)
            continue


def choose(x, a):
    # projectile choosing function
    while True:
        print('\nthere are', len(p["gravity"]), 'projectiles to choose from')

        try:
            choice = int(input('\nchoose a projectile from 1-' + str(len(p["gravity"])) + ' to ' + x + ' : '))
            choice = choice - 1
            display(choice, a)

        # error handling
        except (IndexError, ValueError):
            print(err)
            continue

        return choice


def delete(c):
    # deletes specified projectile values from each key/value pair in projectile dictionary
    for k, v in p.items():
        v.pop(c)


def new():
    # iteration
    for k, v in p.items():

        # error handling while loop
        while True:

            try:
                val = float(input('\nenter a value for ' + k + ': '))

            except ValueError:
                print(err)

                continue
            v.append(val)
            break

    display(len(p['gravity'])-1, 'displayed')

    while True:
        yn = input('\nedit new projectile? before finalizing? (y/n): ')

        if yn == 'y':
            edit(len(p['gravity'])-1)
            print('\nnew projectile added!')
            break

        elif yn == 'n':
            print('\nnew projectile added!')
            break

        else:
            print('\ninvalid input')
            continue


def main():
    # choosing menu
    while True:
        inpt = input(
            '\n(c)hoose existing projectile, (i)nput new projectile, (e)dit existing projectile, or (d)elete existing projectile: ')

        # input new projectile values to be added in dictionary
        if inpt == 'i':
            new()

        # checks if dictionary is empty, can only access following functions if there is a projectile available
        elif len(p['gravity']) > 0:

            # view/display projectile
            if inpt == 'c':
                simulate(choose('view or simulate', 'viewed or simulated'))

            # edit existing values within the dictionary
            elif inpt == 'e':
                edit(choose('edit', 'edited'))

            # delete existing values within dictionary
            elif inpt == 'd':
                delete(choose('delete', 'deleted'))

            # error handling
            else:
                print(err)

        else:
            print(no)
            continue


# dictionary with all projectiles

p = {
    "gravity": [9.8, 9.8],
    "velocity": [50, 50],
    "angle": [45, 60],
    "starting height": [0, 0],
    "ground level": [0, 0],
    "timeframe": [10, 10]
}

# repetitive error statements
err = '\ninvalid input'
no = '\nno projectiles available, please (i)nput a new one'

print('This program simulates a projectile given certain values.')
main()
