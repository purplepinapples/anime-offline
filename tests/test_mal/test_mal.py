import pytest
import requests
import jikanpy

from animeoffline import *
from animeoffline import config
from animeoffline import utils


def test_local_jikan():
    j = jikanpy.Jikan(selected_base=config.jikan_url)
    assert "Cowboy Bebop" == j.anime(1)["title"]
    utils.wait()
