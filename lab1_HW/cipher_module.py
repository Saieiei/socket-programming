# cipher_module.py

def caesar_cipher(message, key):
    result = ""

    for char in message:
        if char.isalpha():
            # Convert character to integer (0-indexed)
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            char_index = ord(char) - base  # 0-indexed

            # Apply Caesar cipher formula
            encrypted_index = (char_index + key) % 26

            # Convert back to character
            encrypted_char = chr(base + encrypted_index)

            # Append to result string
            result += encrypted_char
        else:
            # If the character is not an alphabet character, leave it unchanged
            result += char

    return result

def caesar_decipher(encrypted_message, key):
    decrypted_result = ""

    for char in encrypted_message:
        if char.isalpha():
            # Convert character to integer (0-indexed)
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            char_index = ord(char) - base

            # Apply Caesar decipher formula
            decrypted_index = (char_index - key) % 26

            # Convert back to character
            decrypted_char = chr(base + decrypted_index)

            # Append to decrypted result string
            decrypted_result += decrypted_char
        else:
            # If the character is not an alphabet character, leave it unchanged
            decrypted_result += char

    return decrypted_result
