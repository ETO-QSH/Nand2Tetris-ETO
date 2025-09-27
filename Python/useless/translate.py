from PIL import Image
import csv


color_map = {
    '#9ead85': -1,
    '#8b9876': 0,
    '#141414': 1
}


def read_image(image_path):
    return Image.open(image_path)


def convert_pixels(image, color_map):
    pixels = image.load()
    width, height = image.size
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = pixels[x, y]
            hex_color = '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])
            row.append(color_map.get(hex_color, None))  # 如果颜色不在字典中，返回None
        result.append(row)
    return result


def save_to_csv(data, output_path):
    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def main(image_path):
    image = read_image(image_path)
    converted_data = convert_pixels(image, color_map)
    output_path = image_path.replace('.png', '.csv').replace('png', 'csv')
    save_to_csv(converted_data, output_path)
    print(f"Data saved to {output_path}")


if __name__ == "__main__":
    image_path = './png/' + 'variable.png'
    main(image_path)
