# O(n) time | O(n) space
def caesar_cipher_encryptor(string, key):
    # Write your code here.
    encrypted_array = []
    for character in string:
        cipher_value = get_cipher_index(character, key)
        encrypted_array.append(cipher_value)
    return ''.join(encrypted_array)


def get_cipher_index(character, key):
    all_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_index = all_alphabet.index(character) + key
    cipher_index = cipher_index % 26
    return all_alphabet[cipher_index]


print(caesar_cipher_encryptor('xyz', 2))


