import os


def get_file_size(path: str):
    return os.path.getsize(path)


def get_file_modification_date(path: str):
    return os.path.getmtime(path)
