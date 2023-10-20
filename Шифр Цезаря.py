
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("А") if char.isupper() else ord("а")
            shifted_char = chr((ord(char) - ascii_offset + shift) % 32 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def encrypt():
    text = text_entry.get()
    shift = int(shift_var.get())
    result = caesar_cipher(text, shift)
    result_label.config(text=result)

def decrypt():
    text = text_entry.get()
    shift = int(shift_var.get())
    result = caesar_cipher(text, -shift)
    result_label.config(text=result)

root = Tk()
root.title("Шифр Цезаря")

text_label = Label(root, text="Текст:")
text_label.grid(row=0, column=0, padx=20, pady=20)

text_entry = Entry(root)
text_entry.grid(row=0, column=1, padx=10, pady=10)

shift_label = Label(root, text="Сдвиг:")
shift_label.grid(row=1, column=0, padx=10, pady=10)

shift_var = StringVar(root)
shift_choices = list(map(str, range(1, 33)))
shift_menu = OptionMenu(root, shift_var, *shift_choices)
shift_menu.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = Button(root, text="Зашифровать", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="Расшифровать", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()

