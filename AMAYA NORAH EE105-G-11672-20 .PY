import tkinter as tk

def vigenere_cipher(message, key, encrypt=True):
    result = ""
    key_length = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            start = ord('a') if char.islower() else ord('A')
            if encrypt:
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def encrypt_message(result_label):
    input_msg = entry_message.get()
    key = "AMAYA"
    encrypted_msg = vigenere_cipher(input_msg, key)
    result_label.config(text=f"Encrypted message: {encrypted_msg}")

def decrypt_message(result_label):
    input_msg = entry_message.get()
    key = "AMAYA"
    decrypted_msg = vigenere_cipher(input_msg, key, encrypt=False)
    result_label.config(text=f"Decrypted message: {decrypted_msg}")

# GUI part
window = tk.Tk()
window.title("Vigenère Cipher Encryption/Decryption")

# Message entry
label_msg = tk.Label(window, text="Enter message:")
label_msg.grid(row=1, column=1)
entry_message = tk.Entry(window)
entry_message.grid(row=1, column=2)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", bg="blue", fg="white", command=lambda: encrypt_message(result_label))
encrypt_button.grid(row=2, column=1)

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", bg="red", fg="white", command=lambda: decrypt_message(result_label))
decrypt_button.grid(row=2, column=2)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=1, columnspan=2)

window.mainloop()
