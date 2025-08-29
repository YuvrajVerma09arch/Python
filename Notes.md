# Cryptographic Ciphers in Python

A simple command-line tool for encrypting messages using classical cipher algorithms, created as part of my journey into Python and software development.

---

## Features
* **Caesar Cipher:** Encrypts messages by shifting letters a fixed number of places down the alphabet.
* **Vigenère Cipher:** A more advanced cipher that uses a keyword to apply a series of different Caesar ciphers.

---

## How It Works

### The Caesar Cipher
This cipher is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on.

### The Vigenère Cipher
This cipher enhances the Caesar cipher by using a keyword instead of a simple number. Each letter of the keyword corresponds to a different shift value, making the encryption much harder to break. For example, if the key is 'KEY', the first letter is shifted by 'K' (10), the second by 'E' (4), the third by 'Y' (24), and then it repeats.

---

## How to Use
1.  Ensure you have Python 3 installed.
2.  Navigate to the `cryptography-ciphers` directory in your terminal.
3.  Run the script with the following command:
    ```bash
    python3 ciphers.py
    ```
4.  The program will then prompt you to enter a message and the required keys for each cipher.