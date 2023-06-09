import glob
import os

from inverted_index import InvertedIndex
import lict_data


def get_files_list(root, extension):
    paths = glob.glob(f'**/*{extension}', root_dir=root, recursive=True)
    # Filter out directories
    paths = [path for path in paths if not os.path.isdir(os.path.join(root, path))
             and not path.endswith(InvertedIndex.extension)
             and not path.endswith(lict_data.LictConfig.filename_extension)]
    return paths


def get_movie_list(root):
    return get_files_list(root, '.txt')


def get_index_files(root):
    movies = glob.glob(f'**/*{InvertedIndex.extension}', root_dir=root, recursive=True)
    return movies


def write_file(path, text):
    file = os.path.basename(path)
    os.chdir(path.removesuffix(os.path.basename(path)))
    with open(file, "wt") as f:
        f.write(text)


def read_file(path):
    file = os.path.basename(path)
    os.chdir(path.removesuffix(os.path.basename(path)))
    with open(os.path.basename(path), "r") as f:
        text = f.read()
        return text


def get_modification_date(path):
    fpath = os.path.join(os.path.dirname(__file__), path)
    size = os.path.getsize(fpath)
    ctime = os.path.getctime(fpath)
    return size, ctime
