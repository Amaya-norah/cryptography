import tkinter as tk
import random

# Function to generate a random substitution cipher key
def generate_cipher_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    cipher_key = dict(zip(alphabet, shuffled_alphabet))
    return cipher_key

# Function to encrypt a message using a substitution cipher
def encrypt_message(message, cipher_key):
    encrypted_msg = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_msg += cipher_key[char]
            else:
                encrypted_msg += cipher_key[char.lower()].upper()
        else:
            encrypted_msg += char
    return encrypted_msg

# Function to handle encryption button click event
def encrypt_button_click():
    input_msg = entry_message.get()
    encrypted_msg = encrypt_message(input_msg, cipher_key)
    result_label.config(text=f"Encrypted message: {encrypted_msg}")

 # Function to decrypt a message using a substitution cipher
def decrypt_message(encrypted_message, cipher_key):
    decrypted_msg = ''
    reverse_cipher_key = {v: k for k, v in cipher_key.items()}  # Creating a reverse mapping
    
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted_msg += reverse_cipher_key[char]
            else:
                decrypted_msg += reverse_cipher_key[char.lower()].upper()
        else:
            decrypted_msg += char
    return decrypted_msg


# Generate a random substitution cipher key
cipher_key = generate_cipher_key()

# GUI part
window = tk.Tk()
window.title("Random Substitution Cipher Encryption")

# Message entry
label_msg = tk.Label(window, text="Enter message")
label_msg.grid(row=1, column=1)
entry_message = tk.Entry(window)
entry_message.grid(row=1, column=2)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", bg="red", fg="white", command=encrypt_button_click)
encrypt_button.grid(row=3, column=1, columnspan=2)

# Function to handle decryption button click event
def decrypt_button_click():
    encrypted_msg = entry_message.get()
    decrypted_msg = decrypt_message(encrypted_msg, cipher_key)
    result_label.config(text=f"Decrypted message: {decrypted_msg}")

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", bg="blue", fg="white", command=decrypt_button_click)
decrypt_button.grid(row=3, column=1, columnspan=2, sticky='E')

# Result label
result_label = tk.Label(window, text=" ")
result_label.grid(row=5, column=1, columnspan=2)

window.mainloop()
