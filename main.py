alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % 26
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Function to ask user if they want to restart the program
def restart_program():
    while True:
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == "yes":
            return True
        elif restart == "no":
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Importing and printing the logo
from art import logo
print(logo)

# Main program loop
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Handling shifts greater than 26
    shift %= 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    if not restart_program():
        break
