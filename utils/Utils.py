import os
import keyword


class Utils:
    @staticmethod
    def create_package(package_path):
        if os.path.exists(package_path):
            return

        os.makedirs(package_path, exist_ok=True)
        with open(os.path.join(package_path, '__init__.py'), 'w') as f:
            pass

    @staticmethod
    def is_valid_identifier(name):
        return name.isidentifier() and not keyword.iskeyword(name)
