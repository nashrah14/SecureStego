from PIL import Image

def embed_data(image_path, output_path, data):
    img = Image.open(image_path)
    data += "<END>"  # custom delimiter to mark end of message
    binary_data = ''.join(format(ord(i), '08b') for i in data)
    data_index = 0
    pixels = list(img.getdata())

    new_pixels = []
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # only RGB
            if data_index < len(binary_data):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))
        if data_index >= len(binary_data):
            new_pixels.extend(pixels[len(new_pixels):])
            break

    img.putdata(new_pixels)
    img.save(output_path)
