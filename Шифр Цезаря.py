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


def encrypt(text, shift):
    return caesar_cipher(text, shift)


def decrypt(text, shift):
    return caesar_cipher(text, -shift)


def main():
    text = input("Введите текст: ")
    shift = int(input("Введите шаг сдвига: "))
    choice = input("Шифрование (1) или расшифровка (2): ")

    if choice == "1":
        result = encrypt(text, shift)
        print("Зашифрованный текст:", result)
    elif choice == "2":
        result = decrypt(text, shift)
        print("Расшифрованный текст:", result)
    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()