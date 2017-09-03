# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# This is a simple cryptographic tool based on caesar cipher algorithm.
# I took out this example from the book: Hacking Secret Ciphers with Python - Invent with Python
# I made a bit of change to the original version, by getting input from user.
# pyperclip is a module created by the author of the book. Put the pyperclip file in the same folder of the main file.

import pyperclip

# the string to be encrypted/decrypted

message = input("Only Alphabetical Characters Allowed [A-Z] - CHARACTERS OUT OF THIS RANGE WON'T BE ENCRYPTED.\n"+"Enter your message: ")              

# the encryption/decryption key

while True:
    key = int(input("Choose a key, numbers between[1-25]: "))
    if not(key > 25 or key < 1):
        break
    
# tells the program to encrypt or decrypt
mode = input("Enter the mode -- 'encrypt' or 'decrypt': ") # set to 'encrypt' or 'decrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)
