import os
import directory_search


def get_file_size(path: str):
    return os.path.getsize(path)


def get_file_modification_date(path: str):
    return os.path.getmtime(path)


def file_changes(root_path: str, config, extension):
    """
    Finds all the files that have been changed since the last index built
    """
    # The relative path from the root
    file_paths = directory_search.get_files_list(root_path, extension)
    # The full path to the movies
    file_paths_full = [os.path.join(root_path, p) for p in file_paths]
    # Combine since we need the absolute path to open the file but relative for tree and index
    paths_tuple = zip(file_paths_full, file_paths)

    # Setup for deleted
    # Remove the keys as we iterate. Anything leftover has been deleted
    deleted = set(config.index_changes_dict.keys())

    # Check for file changes relative to the previously built index (if there is one)
    # Performance can be improved by using a generator
    paths_to_index = []
    for paths in paths_tuple:
        f_path = paths[0]
        file_id = paths[1]
        should_index = config.should_index(f_path, file_id)
        if should_index:
            paths_to_index.append(paths)

        deleted.discard(file_id)

    deleted = [os.path.join(root_path, p) for p in deleted]
    return paths_to_index, deleted


def load_document(f_path, id):
    with open(f_path, 'r', encoding="utf8", errors='ignore') as textfile:
        data = textfile.read().replace('\n', ' ').strip()
        return {
            'id': id,
            'text': data
        }
