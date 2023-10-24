# Written by G. Renault - 10/03/23
# This script implements the hashing algo. of the modbus/UMAS protocol used by Unity Pro and illustrates how to find a collision.
# Code taken from: "Examining Crypto and Bypassing Authentication in Schneider Electric PLCs (M340/M580)"
# https://medium.com/tenable-techblog/examining-crypto-and-bypassing-authentication-in-schneider-electric-plcs-m340-m580-f37cf9f3ff34
# All credits go to Nicholas Miles from tenable.

import random
import string
import time

# Credit to Nicholas Miles
def calc_pass_char(tmp):
    if tmp % 2 == 0:
        return (tmp % 0x1A) + 0x41
    else:
        return ord(format(tmp % 0x10, "X"))


# Credit to Nicholas Miles
def crypt_pass(password):
    res_str = ""
    local_c0 = 0

    pwd_data = password.encode("utf-16")[2:]

    for i in range(0, len(password)):
        local_6 = pwd_data[(i * 2) - 1]
        local_5 = pwd_data[i * 2]

        local_14 = 0
        for j in range(0, i):
            local_14 = local_14 + pwd_data[j * 2]

        local_10 = 0
        for k in range(i + 1, len(password)):
            local_10 = local_10 + pwd_data[k * 2]

        if local_5 / 2 < local_6:
            local_c0 = calc_pass_char(
                (local_5 + 1) * (local_6 + 1) + local_c0 + local_10
            )
            res_str += chr(local_c0)

        local_c0 = calc_pass_char(
            local_c0 * i + local_5 * (i + 1) + local_6 * (i + 2) + local_14 + local_10
        )

        res_str += chr(local_c0)

    return res_str


print(f"enc(password) = {crypt_pass('password')}")


def find_a_collision(len_):
    collision = False
    plaintext_pwd = []
    ciphertext_pwd = []
    while not collision:
        random_pwd = "".join(
            random.choice(string.ascii_uppercase + string.digits) for i in range(len_)
        )
        if random_pwd not in plaintext_pwd:
            plaintext_pwd += [random_pwd]
            ciphertext_pwd += [crypt_pass(random_pwd)]

            if len(set(ciphertext_pwd)) < len(ciphertext_pwd):
                print("Collision found")
                collision = True


# Find a collision of any two words of length l
l = 8
find_a_collision(l)

# Find a collision of a given word
init_time = time.time()


def find_collision(password):
    collision = False
    ciphertext_1_pwd = crypt_pass(password)
    n = 0
    while (not collision) and n < 10**7:
        n += 1
        random_pwd = "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for i in range(len(password))
        )
        ciphertext_2_pwd = crypt_pass(random_pwd)

        if ciphertext_2_pwd == ciphertext_1_pwd:
            print("Collision found")
            collision = True

    loop_time = time.time() - init_time
    print(f"Time taken : {loop_time}")


find_collision("password")
