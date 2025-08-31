# ciphers.py

def caesar_encrypt(message, offset):
    """
    Encrypts a message using the Caesar cipher.

    Args:
        message (str): The plaintext message to encrypt.
        offset (int): The number of positions to shift letters.

    Returns:
        str: The encrypted ciphertext.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            # The modulo operator (%) ensures the index wraps around the alphabet
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

def vigenere_encrypt(message, key):
    """
    Encrypts a message using the Vigenère cipher.

    Args:
        message (str): The plaintext message to encrypt.
        key (str): The keyword for the cipher.

    Returns:
        str: The encrypted ciphertext.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

# This is the main part of the program that runs when you execute the file
if __name__ == "__main__":
    print(" Welcome to the Ancient Cipher Toolkit!")
    
    # Get user input
    text_to_process = input("Enter the message you want to encrypt: ")
    
    # Encrypt with Caesar Cipher
    try:
        shift = int(input("Enter a number to be the Caesar shift key (e.g., 3): "))
        caesar_encrypted = caesar_encrypt(text_to_process, shift)
        print(f"\nCaesar Encrypted Text: {caesar_encrypted}")
    except ValueError:
        print("\nInvalid shift value. It must be a number.")

    # Encrypt with Vigenère Cipher
    vigenere_key = input("\nEnter a word to be the Vigenère key (e.g., 'python'): ")
    if vigenere_key.isalpha():
        vigenere_encrypted = vigenere_encrypt(text_to_process, vigenere_key)
        print(f"Vigenère Encrypted Text: {vigenere_encrypted}")
    else:
        print("Invalid key. The Vigenère key must only contain letters.")

# verification of CardNumber using Luhn Algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4511-3532-45-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


if __name__ == '__main__':
    main()
