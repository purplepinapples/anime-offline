import requests
from jikanpy import Jikan

from animeoffline import *
from animeoffline import config
from animeoffline import utils

# if anime_offline/config.py is unedited, this assumes a local instance
# of jikan-rest is running on your system
# https://github.com/jikan-me/jikan-rest

jikan = Jikan(selected_base=config.jikan_url)
