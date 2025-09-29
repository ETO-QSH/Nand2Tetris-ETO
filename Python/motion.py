from activate import tetromino


def rpng_random(seed):
    temp1 = seed >> 1
    temp2 = seed ^ temp1
    temp3 = temp2 << 1
    temp4 = temp2 ^ temp3
    temp5 = temp4 >> 2
    seed = temp4 ^ temp5
    result = seed % 7
    return result, seed


def get_row16(db, row):
    hi, lo = db[row * 2], db[row * 2 + 1]
    return (hi << 8) | lo


def set_row16(db, row, val16):
    db[row * 2] = (val16 >> 8) & 0xFF
    db[row * 2 + 1] = val16 & 0xFF


def cells(p):
    return [(p[1] + dx, p[2] + dy) for (dx, dy) in tetromino[p[0]][p[3]]]


def hit(db, p):
    for x, y in cells(p):
        if x < 0 or x >= 10 or y < 0 or y >= 20:  # 越界
            return True
        if get_row16(db, y) & (1 << x):  # 已被占
            return True
    return False


def place(db, p):
    for x, y in cells(p):
        set_row16(db, y, get_row16(db, y) | (1 << x))


def erase(db, p):
    for x, y in cells(p):
        set_row16(db, y, get_row16(db, y) & ~(1 << x))


def move(db, p, dx, dy):
    erase(db, p)
    old_x, old_y = p[1], p[2]
    p[1] += dx
    p[2] += dy
    if hit(db, p):  # 撞了回退
        p[1], p[2] = old_x, old_y
        place(db, p)
        return False
    place(db, p)
    return True


def rotate(db, p, r):
    erase(db, p)
    old_rot = p[3]
    p[3] = (p[3] + r) & 3
    if hit(db, p):  # 撞了回退
        p[3] = old_rot
        place(db, p)
        return False
    place(db, p)
    return True


def clear_lines(db, lines):
    for r in lines:
        for rr in range(r, 0, -1):
            set_row16(db, rr, get_row16(db, rr - 1))
        set_row16(db, 0, 0)


def find_full_rows(db, p):
    rows = {y for _, y in cells(p)}
    return [r for r in sorted(rows) if get_row16(db, r) == 0x3FF]
