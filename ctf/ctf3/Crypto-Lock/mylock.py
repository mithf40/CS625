#encoding=utf-8
import random
from Crypto import Random
from Crypto.Cipher import AES
import os

IV = "\x42" * AES.block_size


encrypted_file = "secret.docx.enc"


def generate_key(size,a):
    key = bytearray()
    random.seed(a)
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def unpad(p):
    return p[0:-ord(p[-1])]

def decrypt(key,data):
    data = data.decode("hex")
    cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    m = cipher.decrypt(data)
    return m


def main():
    with open(encrypted_file, 'r') as f:
        ciphertext = f.read()
    b=1523017351
    # b = 1523710412
    for a in range(b,b-30,-1):        
        key = generate_key(32,a)
        plaintext = decrypt(key, ciphertext)
        plaintext_file = "secret"+str(b-a+1)+".docx"
        with open(plaintext_file, 'w') as f:
            f.write(plaintext)
        # print(plaintext)

    # 😈
    # os.remove(plaintext_file)

if __name__ == "__main__":
    main()

