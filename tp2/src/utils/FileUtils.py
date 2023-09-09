import os

class FileUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    @classmethod
    def exists(cls, path: str): 
        return os.path.exists(path)

    @classmethod
    def exists_or_create_dir(cls, path: str) -> bool:
        if cls.exists(path): return False

        os.makedirs(path)
        return True
