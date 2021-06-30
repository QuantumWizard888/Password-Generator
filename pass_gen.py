
###* Simple password generator
###? How to use ###
#? Generate password of particular length:
#* python3 pass_gen PASSWORD_LENGTH
#? Generate list of N passwords of particular length:
#* python3 pass_gen PASSWORD_LENGTH QUANTITY_OF_PASSWORDS
#! PASSWORD_LENGTH - default value is 16, for security reasons consider values >=16 (20 is recommended)

import random
import sys

symbols = 'abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+\|~`[];:'
pass_length = 16

def is_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def pwd_gen(pwd_length):

    return ''.join([random.choice(symbols) for _ in range(int(pwd_length))])

def pwd_list_gen(pwd_length, pwd_quantity):

    for _ in range(int(pwd_quantity)):
        print(pwd_gen(pwd_length))


if len(sys.argv) == 2:
    
    if is_int(sys.argv[1]) is True and int(sys.argv[1]) > 0:
        print('>>> Generating password with PASSWORD_LENGTH = %s\n' % sys.argv[1])
        print(pwd_gen(sys.argv[1]))
    else:
        print('[ERROR!] Invalid PASSWORD_LENGTH value!')

elif len(sys.argv) == 3:
    
    if is_int(sys.argv[1]) is True and int(sys.argv[1]) > 0 and is_int(sys.argv[2]) is True and int(sys.argv[2]) > 0:
        print('>>> Generating list of %s passwords with PASSWORD_LENGTH = %s\n' % (sys.argv[2], sys.argv[1]))
        pwd_list_gen(sys.argv[1], sys.argv[2])
    else:
        print('[ERROR!] Invalid PASSWORD_LENGTH/QUANTITY_OF_PASSWORDS (or both) value!')


elif len(sys.argv) < 2:
    print('>>> Generating password with default PASSWORD_LENGTH = 16')
    print(pwd_gen(pass_length))