def encrypt(text, key):
    encrypted_text = ''
    alphabet, encrypted_alphabet = get_alphabet(key)

    for char in text:
        if char == ' ': encrypted_text += ' '
        else:  encrypted_text += encrypted_alphabet[alphabet.index(char)]
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ''
    alphabet, encrypted_alphabet = get_alphabet(key)

    for char in text:
       if char == ' ': decrypted_text += ' '
       else:  decrypted_text += alphabet[encrypted_alphabet.index(char)]
    return decrypted_text

def get_alphabet(key):
    alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
    encrypted_alphabet = []
    for i in range(len(alphabet)):
        if i < key: encrypted_alphabet.append(alphabet[i])
        else:  encrypted_alphabet.insert(encrypted_alphabet.index('a'), alphabet[i])
    return alphabet, encrypted_alphabet

# testing \/
a = 'hello world'
b = encrypt(a, 5)
c = decrypt(b, 5)

print a
print b
print c
