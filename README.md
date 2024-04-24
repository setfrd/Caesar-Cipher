# Caesar Cipher

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

This Python program implements a Caesar Cipher encryption and decryption tool. It allows the user to input a message, specify the shift amount, and choose whether to encrypt or decrypt the message.

## Features

- Encryption: Shifts each letter of the message forwards in the alphabet by the specified amount.
- Decryption: Shifts each letter of the message backwards in the alphabet by the specified amount.
- Handles shifts greater than 26 by wrapping around the alphabet.
- Maintains numbers, symbols, and spaces unchanged in the encrypted/decrypted message.
- Provides an option to restart the program to encrypt/decrypt another message.
- Displays an ASCII art logo at the start of the program.

## Usage

1. Run the program (`caesar_cipher.py`).
2. Follow the on-screen prompts:
   - Choose 'encode' to encrypt or 'decode' to decrypt.
   - Enter your message.
   - Enter the shift number.
3. The program will display the encrypted or decrypted message.
4. Choose 'yes' to restart the program or 'no' to exit.

## Files

- `caesar_cipher.py`: The main Python script containing the Caesar Cipher implementation.
- `art.py`: A separate file containing ASCII art used for the program logo.

## Dependencies

This program requires Python 3.x to run.

## Notes

- The program handles only lowercase letters. Uppercase letters are converted to lowercase before encryption/decryption.
- Non-alphabetic characters such as numbers, symbols, and spaces are maintained unchanged in the encrypted/decrypted message.
