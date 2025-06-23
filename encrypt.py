from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

def pad_message(msg):
    pad_len = 16 - len(msg) % 16
    return msg + (chr(pad_len) * pad_len)

def unpad_message(msg):
    pad_len = ord(msg[-1])
    return msg[:-pad_len]

def encrypt_message(message, password):
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad_message(message).encode())
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_message(enc_message, password):
    enc = base64.b64decode(enc_message)
    iv = enc[:16]
    ct = enc[16:]
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    return unpad_message(pt.decode())
