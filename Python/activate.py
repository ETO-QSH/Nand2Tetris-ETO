from divide import result_dict

block_matrix = [[(9 + 8 * x, 9 + 8 * y) for x in range(10)] for y in range(20)]
# print(block_matrix)

bool_matrix = {
    "NEXT": [(93, 25), (101, 25), (109, 25), (117, 25), (93, 33), (101, 33), (109, 33), (117, 33)],
    "SAVE": [(93, 57), (101, 57), (109, 57), (117, 57), (93, 65), (101, 65), (109, 65), (117, 65)],
    "DIFF": [(93, 89), (101, 89), (109, 89), (117, 89)],
    "arrow": [(82, 124), (82, 134)],
    "cat": [(105, 154)]
}
# print(bool_matrix)

num_matrix = [(93, 113), (101, 113), (109, 113), (117, 113), (93, 137), (101, 137), (109, 137), (117, 137)]
# print(num_matrix)

block_type = {
    "I": 0b00001111, "J": 0b10001110, "L": 0b00101110, "O": 0b11001100, "S": 0b01101100, "T": 0b01001110, "Z": 0b11000110
}  # 15 142 46 204 108 78 198

tetromino = {
    15: [                                     # I
        [(0, 0), (-2, 0), (-1, 0), (1, 0)],   # 0°
        [(0, 0), (0, -2), (0, -1), (0, 1)],   # 90°
        [(0, 0), (-2, 0), (-1, 0), (1, 0)],   # 180°
        [(0, 0), (0, -2), (0, -1), (0, 1)]    # 270°
    ],
    142: [                                    # J
        [(0, 0), (-1, 0), (1, 0), (-1, 1)],   # 0°
        [(0, 0), (0, -1), (0, 1), (-1, -1)],  # 90°
        [(0, 0), (-1, 0), (1, 0), (1, -1)],   # 180°
        [(0, 0), (0, -1), (0, 1), (1, 1)]     # 270°
    ],
    46: [                                     # L
        [(0, 0), (-1, 0), (1, 0), (1, 1)],    # 0°
        [(0, 0), (0, -1), (0, 1), (1, -1)],   # 90°
        [(0, 0), (-1, 0), (1, 0), (-1, -1)],  # 180°
        [(0, 0), (0, -1), (0, 1), (-1, 1)]    # 270°
    ],
    204: [                                    # O
        [(0, 0), (0, 1), (1, 0), (1, 1)],     # 0°
        [(0, 0), (0, 1), (1, 0), (1, 1)],     # 90°
        [(0, 0), (0, 1), (1, 0), (1, 1)],     # 180°
        [(0, 0), (0, 1), (1, 0), (1, 1)]      # 270°
    ],
    108: [                                    # S
        [(0, 0), (-1, 0), (0, 1), (1, 1)],    # 0°
        [(0, 0), (0, -1), (-1, 0), (-1, 1)],  # 90°
        [(0, 0), (-1, 0), (0, 1), (1, 1)],    # 180°
        [(0, 0), (0, -1), (-1, 0), (-1, 1)]   # 270°
    ],
    78: [                                     # T
        [(0, 0), (-1, 0), (1, 0), (0, 1)],    # 0°
        [(0, 0), (0, -1), (0, 1), (-1, 0)],   # 90°
        [(0, 0), (-1, 0), (1, 0), (0, -1)],   # 180°
        [(0, 0), (0, -1), (0, 1), (1, 0)]     # 270°
    ],
    198: [                                    # Z
        [(0, 0), (1, 0), (0, 1), (-1, 1)],    # 0°
        [(0, 0), (0, -1), (1, 0), (1, 1)],    # 90°
        [(0, 0), (1, 0), (0, 1), (-1, 1)],    # 180°
        [(0, 0), (0, -1), (1, 0), (1, 1)]     # 270°
    ]
}

text_matrix = [
    [(42, 124, "S"), (50, 124, "T"), (58, 124, "A"), (66, 124, "R"), (74, 124, "T")],
    [(42, 134, "L"), (50, 134, "E"), (58, 134, "V"), (66, 134, "E"), (74, 134, "L")],
    [(93, 17, "N"), (101, 17, "E"), (109, 17, "X"), (117, 17, "T")],
    [(93, 49, "S"), (101, 49, "A"), (109, 49, "V"), (117, 49, "E")],
    [(93, 81, "D"), (101, 81, "I"), (109, 81, "F"), (117, 81, "F")],
    [(93, 105, "S"), (101, 105, "C"), (109, 105, "O"), (117, 105, "R")],
    [(93, 129, "B"), (101, 129, "E"), (109, 129, "S"), (117, 129, "T")],
]


def text_matrix_spliter(byte: int):
    last_7_bits = byte & 0x7F
    bool_list = [(last_7_bits >> i) & 1 for i in range(6, -1, -1)]

    activate_pixiv = []
    for i, j in enumerate(bool_list):
        if j:
            for ox, oy, s in text_matrix[i]:
                for x, y in list(result_dict[s]):
                    activate_pixiv.append((ox + x, oy + y))

    return activate_pixiv


def bool_matrix_spliter(NEXT: int, SAVE: int, byte: int):
    last_8_bits = byte & 0xFF
    bool_list = [(last_8_bits >> i) & 1 for i in range(7, -1, -1)]

    activate_pixiv = []
    for i, j in enumerate(bool_list[1: 2]):
        if j:
            ox, oy = bool_matrix["cat"][i]
            for x, y in list(result_dict["cat"]):
                activate_pixiv.append((ox + x, oy + y))
    for i, j in enumerate(bool_list[2: 4]):
        if j:
            ox, oy = bool_matrix["arrow"][i]
            for x, y in list(result_dict["arrow"]):
                activate_pixiv.append((ox + x, oy + y))
    for i, j in enumerate(bool_list[4: 8]):
        if j:
            ox, oy = bool_matrix["DIFF"][i]
            for x, y in list(result_dict["diff"]):
                activate_pixiv.append((ox + x, oy + y))

    next_bool_list = [(NEXT >> i) & 1 for i in range(7, -1, -1)]
    save_bool_list = [(SAVE >> i) & 1 for i in range(7, -1, -1)]

    for i, j in enumerate(next_bool_list):
        if j:
            ox, oy = bool_matrix["NEXT"][i]
            for x, y in list(result_dict["pre"]):
                activate_pixiv.append((ox + x, oy + y))
    for i, j in enumerate(save_bool_list):
        if j:
            ox, oy = bool_matrix["SAVE"][i]
            for x, y in list(result_dict["pre"]):
                activate_pixiv.append((ox + x, oy + y))

    return activate_pixiv


def num_matrix_spliter(scor: (int, int), best: (int, int)):
    activate_pixiv = []
    nums = list(str(scor[0] * 256 + scor[1]).zfill(4)) + list(str(best[0] * 256 + best[1]).zfill(4))
    for i, j in enumerate(nums):
        ox, oy = num_matrix[i]
        for x, y in list(result_dict[j]):
            activate_pixiv.append((ox + x, oy + y))
    return activate_pixiv


def _2x8_10_spliter(high: int, low: int):
    combined = (high << 8) | low
    last_10_bits = combined & 0x3FF
    bool_list = [(last_10_bits >> i) & 1 for i in range(9, -1, -1)]
    return bool_list


def _2x8_10_spliter_group(nums: list):
    activate_pixiv = []
    pairs = [nums[i * 2: i * 2 + 2] for i in range(len(nums) // 2)]
    for i, pair in enumerate(pairs):
        for e, j in enumerate(_2x8_10_spliter(*pair)):
            if j:
                ox, oy = block_matrix[i][e]
                for x, y in list(result_dict["block"]):
                    activate_pixiv.append((ox + x, oy + y))
    return activate_pixiv


def activate_register(register: list):
    activate_pixiv = set(
        _2x8_10_spliter_group(register[:40]) +
        num_matrix_spliter(register[40: 42], register[42: 44]) +
        bool_matrix_spliter(register[44], register[45], register[46]) +
        text_matrix_spliter(register[47])
    )
    return activate_pixiv
