import random

def password_gen(passlength):
    c = ""
    chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    # passlength = int(input("Masukkan panjang kata sandi yang diinginkan dalam nomor:"))

    for i in range(passlength):
        a = random.choice(chars)
        c = a + c

    return c

def random_emoji(emojis):
    emojis = [":skull:", ":grinning:", ":money_mouth:", ":nerd:", ":moyai:"]
    return random.choice(emojis)

def roll_dice():
    roll = random.randint(1,6)
    return roll

def flip_coin():
    flip = random.randint(0,1)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
