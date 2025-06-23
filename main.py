from steg.encrypt import encrypt_message, decrypt_message
from steg.embed import embed_data
from steg.extract import extract_data
import sys

def hide():
    image_path = input("Enter path to cover image: ")
    output_path = input("Enter output image path: ")
    message = input("Enter message to hide: ")
    password = input("Enter password: ")

    encrypted = encrypt_message(message + "~~~~~~~", password)
    embed_data(image_path, output_path, encrypted)
    print("Data embedded and image saved as", output_path)

def reveal():
    image_path = input("Enter path to stego image: ")
    password = input("Enter password: ")

    extracted = extract_data(image_path)
    try:
        decrypted = decrypt_message(extracted, password)
        print("Hidden message:", decrypted)
    except:
        print("Failed to decrypt. Wrong password or corrupted data.")

if __name__ == "__main__":
    print("1. Hide Message 2. Reveal Message")
    choice = input("Choose option: ")
    if choice == '1':
        hide()
    else:
        reveal()
