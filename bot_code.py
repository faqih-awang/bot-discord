import random

def password_gen(passlength):
    c = ""
    chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    # passlength = int(input("Masukkan panjang kata sandi yang diinginkan dalam nomor:"))

    for i in range(passlength):
        a = random.choice(chars)
        c = a + c

    return c