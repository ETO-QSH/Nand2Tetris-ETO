from activate import activate_register


database = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 5, 72, 0, 0, 97, 127
]

activate = activate_register(database)
activate_map = [[1 if (x, y) in activate else -1 for x in range(125)] for y in range(169)]

register_2 = [
    0, 0, 0, 48, 0, 24, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 3, 53, 3, 191, 3, 191,
    1, 223, 5, 72, 78, 15, 71, 31
]

activate_2 = activate_register(register_2)
activate_map_2 = [[1 if (x, y) in activate_2 else -1 for x in range(125)] for y in range(169)]
