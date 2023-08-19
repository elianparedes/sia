class FileUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    @staticmethod
    def open_map(map_path):
        try:
            with open(map_path, "r") as map_file:
                map_contents = map_file.read()
        except FileNotFoundError:
            print(f"Map '{map_path}' not found.")
            print("Make sure it is under the resources/maps folder.")
            exit(1)

        return map_contents