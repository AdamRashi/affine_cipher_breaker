import argparse

args = argparse.ArgumentParser(description=
                               'This is a CLI tool to cipher and '
                               'decipher text with affine permutations '
                               'cryptography algorithm, that uses shift '
                               'that defined by formula:'
                               '        <new_letter> = (a * <letter> + b) mod 26     '
                               )

args.add_argument('FilePath', help='Path to file that contains text')
args.add_argument('KeyA', help='Value of key <a>: recommended to have A=3, or A=7', type=int)
args.add_argument('KeyB', help='Value of key <b>: can be in range from 0 to 25', type=int)

args = args.parse_args()

FILE_PATH: str = args.FilePath
A: int = args.KeyA
B: int = args.KeyB


# with open(FILE_PATH, 'r') as file:
    #