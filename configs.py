LETTER_TO_CODE = {
    chr(ord('А') + nbr): nbr for nbr in range(0, ord('Я') - ord('А') + 1)
}

CODE_TO_LETTER = {
    nbr: chr(ord('А') + nbr) for nbr in range(0, ord('Я') - ord('А') + 1)
}

ALPHABET_SIZE = len(LETTER_TO_CODE)

# print(CODE_TO_LETTER)
# print(ALPHABET_SIZE)