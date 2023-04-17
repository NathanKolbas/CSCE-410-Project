import json
import os

from helpers import get_file_size, get_file_modification_date


class LictConfig:
    """
    Class used to store information about the configuration of lic-t
    """

    filename = 'index.config'

    def __init__(self, index_changes_dict=None, *args, **kwargs):
        # Used to store information about the files that were built to track changes
        self.index_changes_dict: dict = {} if index_changes_dict is None else index_changes_dict

        self.deleted = None

    def __repr__(self):
        """
        String representation of the LictConfig object
        """
        return str(self.__dict__)

    @staticmethod
    def open(root_path: str):
        """
        Opens the stored LictConfig and returns the object if it exists. Otherwise, a new one is created.
        """
        file = os.path.join(root_path, LictConfig.filename)
        if not os.path.exists(file):
            return LictConfig()

        with open(file, 'r', encoding="utf8", errors='ignore') as textfile:
            data = textfile.read()
            return LictConfig.from_json(data)

    @staticmethod
    def from_json(data: str):
        json_dict = json.loads(data)
        return LictConfig(**json_dict)

    def to_json_str(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    def save(self, root_path: str) -> None:
        file = os.path.join(root_path, LictConfig.filename)
        with open(file, 'w', encoding="utf8", errors='ignore') as textfile:
            textfile.write(self.to_json_str())

    def should_index(self, f_path, file_id) -> bool:
        if file_id in self.index_changes_dict:
            file_props = self.index_changes_dict[file_id]
            # Compare file props to last built index
            return get_file_size(f_path) != file_props['size'] or \
                get_file_modification_date(f_path) != file_props['modification']
        else:
            # Index not created yet
            return True

    def indexed_file(self, f_path, file_id):
        self.index_changes_dict[file_id] = {
            'size': get_file_size(f_path),
            'modification': get_file_modification_date(f_path),
        }
