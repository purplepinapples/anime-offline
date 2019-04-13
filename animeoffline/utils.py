from time import sleep

from animeoffline import *
from animeoffline import config

def wait(n=3):
    """a wrapper for sleep with a default of three seconds"""
    sleep(n)


def cache(*filepath):
    """Takes a variable number of folder names as input.

    Returns the corresponding cache directory, if it exists
    """
    expected_dir = os.path.join(config.cache_dir, "/".join(filepath))
    if not os.path.exists(expected_dir):
        raise FileNotFoundError("Couldn't find {}".format(expected_dir))
    return expected_dir


def verify_dir_helper(dir):
    """If the directory at `dir` doesnt exist, creates it"""
    if not os.path.exists(dir):
        print("Creating cache directory at {}".format(dir))
        os.makedirs(dir)


def verify_cache_dirs_exists():
    """Makes sure the cache directory at ~/.anime_offline/ exists"""
    verify_dir_helper(config.cache_dir)
    for dir in config._directories:
        verify_dir_helper(dir)

# call whenever this file is imported
verify_cache_dirs_exists()
