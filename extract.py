from PIL import Image

def extract_data(image_path):
    img = Image.open(image_path)
    binary_data = ""
    for pixel in img.getdata():
        for value in pixel[:3]:
            binary_data += str(value & 1)
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte in all_bytes:
        char = chr(int(byte, 2))
        message += char
        if message.endswith("<END>"):
            break
    return message[:-5]  # remove delimiter
