import ast
from string import ascii_lowercase as alc


class LettersUtils:
    @staticmethod
    def load_letters_map_from_file(file_path):
        letters = []

        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                matrix = ast.literal_eval(line)  # Convert string representation of list to actual list
                letters.append(matrix)

        alphabet = []
        for i in alc:
            alphabet.append(i)

        letters_map = {}
        for i, letter in enumerate(letters):
            letters_map[alphabet[i]] = letter

        return letters_map
