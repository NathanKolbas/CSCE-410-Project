from datetime import datetime


class Index:
    """
    Represents the index of an individual file
    including extra data needed about the file
    """

    def __init__(
        self,
        name: str,
        path: str,
        inverted_index: dict | None,
        file_size: int,
        modification_date: datetime,
    ):
        # The name of the file this index is for
        self.name: str = name
        # The file path from the root to this file
        self.path: str = path
        # The inverted index
        self.inverted_index: dict = dict() if inverted_index is None else inverted_index
        # The file size when built
        self.file_size: int = file_size
        # The modification date of the file when built
        self.modification_date: datetime = modification_date

    def __repr__(self):
        """
        String representation of the object
        """
        return str(self.__dict__)
