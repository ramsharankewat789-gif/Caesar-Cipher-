'''
NAME:- Ram Sharan Kewat
Student ID:- 2603775
Module Number:- 4CS001
Module Title:- Introduction To Programming And Problem Solving
Coursework - 1 - Caesar Cipher
'''

import os

def welcome():
    '''
    Displays the welcome message.
    '''
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def encrypt(message, shift):
    '''
    Encrypts a message using Caesar Cipher.
    '''
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    '''
    Decrypts a message using Caesar Cipher.
    '''
    decrypted = ""
    for char in message:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def is_file(filename):
    '''
    Checks whether a file exists.
    '''
    return os.path.isfile(filename)

def process_file(filename, mode, shift):
    '''
    Processes each line in a file.
    '''
    results = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            if mode == "e":
                results.append(encrypt(line, shift))
            else:
                results.append(decrypt(line, shift))
    return results

def write_message(messages):
    '''
    Writes output to results.txt
    '''
    with open("results.txt", "w", encoding="utf-8") as file:
        for message in messages:
            file.write(message + "\n")

def message_or_file():
    '''
    Handles user choices and input.
    '''
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ("e", "d"):
            break
        print("Invalid choice")

    while True:
        choice = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if choice in ("f", "c"):
            break
        print("Invalid choice")

    if choice == "f":
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename")
        message = None
    else:
        action = "encrypt" if mode == "e" else "decrypt"
        message = input(f"What message would you like to {action}: ")
        filename = None

    while True:
        shift = int(input("What is the shift number: "))
        if 0 <= shift <= 25:
            break
        print("Invalid shift")

    return mode, message, filename, shift

def main():
    '''
    Main program controller.
    '''
    welcome()

    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            results = process_file(filename, mode, shift)
            write_message(results)
            print("Output written to results.txt")
        else:
            if mode == "e":
                result = encrypt(message, shift)
            else:
                result = decrypt(message, shift)

            print(result)
            write_message([result])

        while True:
            again = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if again in ("y", "n"):
                break
            print("Invalid input")

        if again == "n":
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()
