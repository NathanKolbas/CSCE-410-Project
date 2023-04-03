import glob


def get_movie_list(root):
    movies = glob.glob('**/*.txt', root_dir=root, recursive=True)
    return movies
