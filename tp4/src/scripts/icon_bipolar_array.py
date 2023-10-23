import os
from src.utils.IconsUtils import IconsUtils

ICONS_PATH = os.path.join(os.pardir, os.pardir, "data", "icons")
ICONS_FILE = os.path.join(ICONS_PATH, os.pardir, "icons.csv")

with open(ICONS_FILE, 'a') as file:
    file_path = os.path.join(ICONS_PATH, "close.png")
    matrix = IconsUtils.get_icon_matrix(file_path)
    flattened_matrix = matrix.flatten()
    print(flattened_matrix)
    file.write("[" + ", ".join(map(str, flattened_matrix)) + "]\n")