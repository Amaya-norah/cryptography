import tkinter as tk

def caesar_cipher(message, shift):
    result = ''
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def encrypt_message():
    input_msg = entry_message.get()
    shift_value = 4
    encrypted_msg = caesar_cipher(input_msg, shift_value)
    result_label.config(text=f"Encrypted message: {encrypted_msg}")

def decrypt_message():
    input_msg = entry_message.get()
    shift_value = -4  # Use the reverse shift for decryption
    decrypted_msg = caesar_cipher(input_msg, shift_value)
    result_label.config(text=f"Decrypted message: {decrypted_msg}")

# GUI part
window = tk.Tk()
window.title("Caesar Cipher Encryption")

# Message entry
label_msg = tk.Label(window, text="Enter message")
label_msg.grid(row=1, column=1)
entry_message = tk.Entry(window)
entry_message.grid(row=1, column=2)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", bg="green", fg="white", command=encrypt_message)
encrypt_button.grid(row=3, column=1)

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", bg="red", fg="white", command=decrypt_message)
decrypt_button.grid(row=3, column=2)

# Result label
result_label = tk.Label(window, text=" ")
result_label.grid(row=4, column=1, columnspan=2)

window.mainloop()
