import csv
from PIL import Image


color_map = {
    -1: (153, 173, 133),  # #9ead85
    0: (139, 152, 118),   # #8b9876
    1: (20, 20, 20)       # #141414
}


def read_and_stack_csvs(csv_paths, activate_map):
    max_width, max_height = 125, 169
    result_data = [[-1 for _ in range(max_width)] for _ in range(max_height)]

    for path in csv_paths:
        with open(path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    if value is not None:
                        result_data[i][j] = max(result_data[i][j], int(value), activate_map[i][j])

    return result_data


def data_to_image(data, color_map):
    width = len(data[0])
    height = len(data)
    pixels = []
    for row in data:
        for value in row:
            pixels.append(color_map[value])

    image = Image.new('RGB', (width, height))
    image.putdata(pixels)
    return image


def overlie(main, data):
    csv_paths = ['background.csv', f'{main}_main.csv']
    csv_paths = ['./csv/' + file for file in csv_paths]
    stacked_data = read_and_stack_csvs(csv_paths, data)
    image = data_to_image(stacked_data, color_map)
    return image
