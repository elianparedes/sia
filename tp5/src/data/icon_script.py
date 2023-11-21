import os
from src.utils.IconsUtils import IconsUtils

ICONS_PATH = os.path.join("../data/small_icons")
ICONS_FILE = os.path.join("small_icons.csv")

with open(ICONS_FILE, 'a') as file:
    for filename in os.listdir(ICONS_PATH):
        file_path = os.path.join(ICONS_PATH, filename)
        matrix = IconsUtils.get_icon_matrix(file_path)
        print(f"{matrix}\n")
        flattened_matrix = matrix.flatten()
        file.write("[" + ", ".join(map(str, flattened_matrix)) + "]\n")