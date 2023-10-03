"""
This module breaks the cryptographic symmetric encryption
algorithm called "Affine permutations". Breaker guessing the keys
using known quantities of letters in given text and the
common quantities of letters in corresponding language
"""
import string

from spellchecker import SpellChecker

from configs import ALPHABET_SIZE, CODE_TO_LETTER, LETTER_TO_CODE
from cryptography import is_coprime, find_reciprocal

RUSSIAN_LETTER_FREQUENCIES = {
    'О': 11.01, 'Е': 8.45, 'А': 7.75, 'И': 7.33, 'Н': 6.70,
    'Т': 6.37, 'С': 5.47, 'Р': 4.73, 'В': 4.54, 'Л': 4.40,
    'К': 3.49, 'М': 3.21, 'Д': 2.98, 'П': 2.81, 'У': 2.62,
    'Я': 2.01, 'Ы': 1.90, 'Ь': 1.74, 'Г': 1.70, 'З': 1.65,
    'Б': 1.52, 'Ч': 1.48, 'Й': 1.21, 'Х': 0.97, 'Ж': 0.94,
    'Ю': 0.64, 'Ш': 0.35, 'Ц': 0.26, 'Щ': 0.17, 'Э': 0.09, 'Ъ': 0.04, 'Ф': 0.02
}


def calculate_chi_squared(observed_frequencies, expected_frequencies, text):
    """
    Calculate the chi-squared statistic to measure the difference
    between observed and expected frequencies.
    """
    chi_squared = 0
    for letter, observed in observed_frequencies.items():
        if letter.isalpha():
            expected = expected_frequencies[letter] * len(text)
            chi_squared += ((observed - expected) ** 2) / expected
    return chi_squared


def affine_break_with_frequency_analysis(ciphertext, misspell_threshold=1):
    """
    Break the Affine cipher using letter frequency analysis for the Russian language.
    """
    results = []

    for key_a in range(1, ALPHABET_SIZE):
        if is_coprime(key_a, ALPHABET_SIZE):
            reciprocal_to_a = find_reciprocal(key_a, ALPHABET_SIZE)
            if reciprocal_to_a is not None:
                for key_b in range(ALPHABET_SIZE):
                    decrypted_text = ''
                    for char in ciphertext:
                        if char.isalpha():
                            original_code = (reciprocal_to_a * (LETTER_TO_CODE[char] - key_b)) % ALPHABET_SIZE
                            decrypted_text += CODE_TO_LETTER[original_code]
                        else:
                            decrypted_text += char

                    results.append(decrypted_text)

    spell = SpellChecker('ru')
    checked_results = []
    for text in results:
        if len(spell.unknown([word.strip(string.punctuation) for word in text.split()])) <= misspell_threshold:
            checked_results.append(text)

    return checked_results
