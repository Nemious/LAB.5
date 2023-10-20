
import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char = char.lower()
            index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_char = alphabet[index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
        else:
            result += char
    return result

def encrypt():
    text = entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift)
    messagebox.showinfo("Результат", "Зашифрованный текст: " + encrypted_text)

def decrypt():
    text = entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, -shift)
    messagebox.showinfo("Результат", "Расшифрованный текст: " + decrypted_text)

window = tk.Tk()
window.title("Шифр Цезаря")
window.geometry("400x600")

label = tk.Label(window, text="Введите текст:")
label.pack()

entry = tk.Entry(window)
entry.pack()

shift_label = tk.Label(window, text="Введите шаг сдвига:")
shift_label.pack()

shift_entry = tk.Entry(window)
shift_entry.pack()

encrypt_button = tk.Button(window, text="Зашифровать", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Расшифровать", command=decrypt)
decrypt_button.pack()

window.mainloop()

