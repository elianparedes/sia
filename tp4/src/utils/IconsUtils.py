import os
import ast
from string import ascii_lowercase as alc
from PIL import Image
import numpy as np

ICONS_PATH = os.path.join(os.pardir, os.pardir, "data", "icons")


class IconsUtils:


    @staticmethod
    def load_icons_map_from_file(file_path):
        ICONS_NAMES = ["thumb_up", "home", "search", "share", "arrow", "person", "delete", "close", "thumb_down", "arrow_right", "arrow_back", "inv_close", "eva_arrow_right", "eva_delete", "eva_home", "eva_person", "eva_share", "lucide_arrow", "lucide_delete", "lucide_home", "lucide_user"]

        icons = []

        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                matrix = ast.literal_eval(line)  # Convert string representation of list to actual list
                icons.append(matrix)

        alphabet = []
        for i in alc:
            alphabet.append(i)

        icons_map = {}
        for i, icon in enumerate(icons):
            icons_map[ICONS_NAMES[i]] = icon

        return icons_map

    @staticmethod
    def get_icon_matrix(icon):

        img = Image.open(os.path.join(ICONS_PATH, icon)).convert('RGBA')
        background = Image.new('RGBA', img.size, (255, 255, 255))
        img = Image.alpha_composite(background, img).convert('L')

        binary_matrix = np.array(img)
        binary_matrix = np.where(binary_matrix > 245, -1, 1)

        return binary_matrix

