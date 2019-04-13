from animeoffline import *

# Project

_home_dir = str(pathlib.Path.home())
cache_dir = os.path.join(_home_dir, ".anime_offline/")

# Directories

_directories = [os.path.join(cache_dir, cache_path) for cache_path in
    [
        "mal/user_cache",
        "mal/anime",
        "mal/manga",
        "mal/character",
        "mal/producer",
        "mal/magazine",
        "anidb/titles",
        "anidb/titles/tmp"
    ]
]

# mal: MyAnimeList

_jikan_rest_url = "localhost"
_jikan_rest_port = 8000
_jikan_rest_version = "v3"
jikan_url = f"http://{_jikan_rest_url}:{_jikan_rest_port}/{_jikan_rest_version}/"

def list_config():
    pprint.pprint({k:v for k, v in globals().items()
                    if not k.startswith("_") and
                    not isinstance(v, types.ModuleType) and
                    type(v) != type and
                    type(v) != type(list_config)
                  })
