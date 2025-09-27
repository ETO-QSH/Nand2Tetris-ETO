import pgzrun
import pygame
import random
from PIL import Image

from motion import *
from overlie import overlie
from activate import activate_register, block_type


WIDTH, HEIGHT = 500, 676

database = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 5, 72, 0, 0, 97, 127
]

activate = activate_register(database)
activate_map = [[1 if (x, y) in activate else -1 for x in range(125)] for y in range(169)]

pil_to_pygame = lambda pil: pygame.image.fromstring(pil.tobytes(), pil.size, pil.mode)
draw = lambda: screen.blit(pygame.transform.scale(current, (WIDTH, HEIGHT)), (0, 0))

pil_image = overlie("title", activate_map)
title = pil_to_pygame(pil_image)

temp = list(range(40))
catch = [0, 0, 0, 0]
state = "title"
current = title
title_mode = 0
pause = False
frame = 60
choice = 0
tick = 1


def update_current(database, main="title"):
    global current
    activate = activate_register(database)
    activate_map = [[1 if (x, y) in activate else -1 for x in range(125)] for y in range(169)]
    current = pil_to_pygame(overlie(main, activate_map))


def update():
    global database, tick, choice, catch, state

    if not pause:
        tick += 1
    elif pause:
        tick = 0

    if state == "over":
        update_current(database, "game")
        if tick % 5 == 0:
            if temp:
                database[temp.pop()] = 255
                database[temp.pop()] = 255
            else:
                if database[40] * 256 + database[41] > database[42] * 256 + database[43]:
                    database[42], database[43] = database[40], database[41]

    if state == "game":
        update_current(database, "game")
        if not database[44]:
            if not choice:
                choice = random.choice(list(block_type.values()))
            database[44] = choice
            choice = 0

        if not catch[0]:
            tick = 1
            trial = [database[44], 5, 0, 0]
            if hit(database, trial):
                database[46] += 64
                state = "over"
                return

            catch = trial
            database[44] = 0
            place(database, catch)

        last_four_bits = database[46] & 0b1111
        count = bin(last_four_bits).count('1')
        if tick % (frame // (2 ** count)) == 1:
            if not move(database, catch, 0, 1):
                lines = find_full_rows(database, catch)
                if lines:
                    db_lower = database[41] + len(lines)
                    if db_lower > 255:
                        database[41] = db_lower - 255
                        database[40] += 1
                    else:
                        database[41] = db_lower
                    clear_lines(database, lines)
                catch = [0, 0, 0, 0]


def on_key_down(key):
    global current, title_mode, state, choice, pause, database
    print(f"Pressed key: {key.name}")

    if state == "title":
        if key == keys.UP and title_mode:
            title_mode = 0
            database[46] += 16
            update_current(database)
        elif key == keys.DOWN and not title_mode:
            title_mode = 1
            database[46] -= 16
            update_current(database)
        elif key == keys.RETURN:
            if not title_mode:
                state = "game"
                database[46] -= 96
                database[47] -= 96
            elif title_mode:
                last_four_bits = database[46] & 0b1111
                count = (bin(last_four_bits).count('1') + 1) % 5
                database[46] = (database[46] & 0b11110000) | int(f"0b0{'1' * count}", 2)
                update_current(database)

    elif state == "game":
        if key == keys.W:
            if not database[45]:
                database[45] = database[44]
                database[44] = 0
            elif database[45]:
                choice = database[44]
                database[44] = database[45]
                database[45] = 0

        if catch[0]:
            if not pause:
                if key == keys.A:
                    move(database, catch, 1, 0)
                if key == keys.D:
                    move(database, catch, -1, 0)
                if key == keys.S:
                    move(database, catch, 0, 1)
                if key == keys.Q:
                    rotate(database, catch, 1)
                if key == keys.E:
                    rotate(database, catch, -1)
                if key == keys.SPACE:
                    while move(database, catch, 0, 1):
                        pass
            if key == keys.ESCAPE:
                if not pause:
                    database[46] += 64
                elif pause:
                    database[46] -= 64
                pause = not pause


pgzrun.go()
