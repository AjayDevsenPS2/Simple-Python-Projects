def caesar(message, offset, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''

    for char in message.lower():
        if char == ' ':
            result_text += char
        else:
            index = alphabet.find(char)
            if mode == 'encrypt':
                new_index = (index + offset) % len(alphabet)
            elif mode == 'decrypt':
                new_index = (index - offset) % len(alphabet)
            result_text += alphabet[new_index]
    return result_text

text = 'Hello Ajay'
shift = 3

encrypted_text = caesar(text, shift, 'encrypt')
print('plain text:', text)
print('encrypted text:', encrypted_text)

decrypted_text = caesar(encrypted_text, shift, 'decrypt')
print('decrypted text:', decrypted_text)
