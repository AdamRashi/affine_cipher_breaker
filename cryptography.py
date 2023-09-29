from configs import CODE_TO_LETTER, LETTER_TO_CODE

ALPHABET_SIZE = 26


def to_cipher(text: str, key_a: int, key_b: int) -> str:
    """
    Returns text, that encrypted using affine permutations
    symmetric cryptography algorithm with given keys <a> and <b>.
    """
    text = text.upper()
    ciphertext = ''
    for letter in text:
        cipher_code = (LETTER_TO_CODE[letter] * key_a + key_b) % ALPHABET_SIZE
        ciphertext += CODE_TO_LETTER[cipher_code]

    return ciphertext


def find_reciprocal(number: int, modulo: int = ALPHABET_SIZE) -> int:
    """
    Returns reciprocal number for given number
    in system with given modulo
    """
    for candidate in range(0, modulo):
        if (number * candidate) % modulo == 1:
            return candidate
    return -1


def to_decipher(text: str, key_a: int, key_b: int):
    """
        Return decrypted text, that is encrypted using affine permutations
        symmetric cryptography algorithm with given keys <a> and <b>.
    """
    reciprocal_to_a = find_reciprocal(key_a, ALPHABET_SIZE)
    decrypted_text = ''
    for letter in text:
        original_code = (reciprocal_to_a * (LETTER_TO_CODE[letter] - key_b)) % ALPHABET_SIZE
        decrypted_text += CODE_TO_LETTER[original_code]

    return decrypted_text
