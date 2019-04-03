
# anime-offline

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

The purpose of this project is to maintain a cache of anime databases incase the websites ever go down, make cross-database scripts easier to write, improve the quality and consistency of said databases, and have a centralized place to put anime related scripts.

### Installation

Installing creates shell scripts that are used to update the local database.

Install `python3.7` (If you wish to keep your own python version as your default, you can use [`pyenv`](https://github.com/pyenv/pyenv)) and [`pipenv`](https://pipenv.readthedocs.io/en/latest/)).

```zsh
$ git clone https://github.com/purplepinapples/anime-offline
$ cd anime-offline
$ pip3 install pipenv
$ pipenv install
$ pipenv shell
$ make install
```

If you end up editing any of the files, running `make` in `anime-offline` will remove any old builds, uninstall and reinstall the package.

#### Scripts:

- ###### `anime_offline_mal`

Since we'll be making a lot of requests, I recommend installing a local instance of [Jikan](https://github.com/jikan-me/jikan-rest) (see below for installation instructions).

It is possible to modify the `jikan_url` in [`config.py`](animeoffline/config.py) to use [api.jikan.moe](http://api.jikan.moe/v3), though due to the sheer amount of requests I'd highly recommend against it to avoid API abuse and 429s.

- ###### `anime_offline_config`

Lists config variables. These can be changed in [config.py](animeoffline/config.py)

### Tests

```zsh
$ pipenv install --dev
$ pipenv shell
$ python3 -m pytest tests --tb=native
# or, if you want to see source files when errors occur:
$ python3 -m pytest
```

### Installing [Jikan](https://github.com/jikan-me/jikan-rest) locally

You can follow the [directions on the Jikan page](https://github.com/jikan-me/jikan-rest#installation), or:

1. [Install PHP](https://secure.php.net/manual/en/install.php)
2. Install [composer](https://getcomposer.org/download/) and [redis](https://redis.io/). If on a Unix system, these can be installed with `apt` or [`brew`](https://brew.sh/)
    - Linux:
      - `sudo apt install redis`
      - `curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer`
    - Mac:
      - Install [`brew`](https://brew.sh/)
      - `brew install composer`
      - `brew install redis`
3. Start the redis server: `sudo service start redis` or `brew services start redis`
4. `git clone https://github.com/jikan-me/jikan-rest.git`
5. `cd jikan-rest`
6. `mv .env.dist .env`
7. `composer install`
8. Start the server: `php -S localhost:<port_number> -t public`
    - Port number should match the output from `$ anime_offline_config`, ([anime_offline/config](anime_offline/config.py)), default is 8000

### Contributing

Feel free to open an [issue](https://github.com/purplepinapples/anime-offline/issues) or a [pull request](https://github.com/purplepinapples/anime-offline/pulls) if you have a suggestion or something to add.
