def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                if mode == 'encrypt':
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                if mode == 'encrypt':
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    # Get user input
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ")

    # Perform encryption or decryption
    if mode.lower() == 'encrypt':
        result = caesar_cipher(text, shift, 'encrypt')
        print("Encrypted text:", result)
    elif mode.lower() == 'decrypt':
        result = caesar_cipher(text, shift, 'decrypt')
        print("Decrypted text:", result)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

