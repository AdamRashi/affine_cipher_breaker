
LETTER_TO_CODE = {
    chr(ord('A') + nbr): nbr for nbr in range(0, ord('Z') - ord('A') + 1)
}

CODE_TO_LETTER = {
    nbr: chr(ord('A') + nbr) for nbr in range(0, ord('Z') - ord('A') + 1)
}
