import json
from divide import result_dict


pixiv_rom = [0 for _ in range(len(result_dict)) for _ in range(2)]


def convert(result_dict):
    global pixiv_rom
    point = len(result_dict) * 2
    for i, (key, value) in enumerate(result_dict.items()):
        pixiv_rom[i * 2] = point
        pixiv_rom[i * 2 + 1] = len(value) * 2
        point += pixiv_rom[i * 2 + 1]
        pixiv_rom += [item for tup in sorted(value) for item in tup]
        result_dict[key] = i * 2
    return result_dict


result_dict = convert(result_dict)
print(len(pixiv_rom), pixiv_rom)
print(result_dict)

# with open("pixiv.json", "w", encoding="utf-8") as file:
#     json.dump(result_dict, file, ensure_ascii=False, indent=4)
