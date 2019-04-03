#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import toml

# get depdencies from Pipfile
with open("Pipfile") as f:
    requires = toml.load(f)

install_requires = []
dependency_links = []
for package, version in requires["packages"].items():
    if version == "*":
        # install most recent version
        install_requires.append(package)
    elif isinstance(version, dict) and 'git' in version:
        # for github repositories
        install_requires.append(package)
        # have github convert git repo requires to tarballs
        if "ref" in version: # if a branch is specified
            dependency_links.append("{}/tarball/{}#egg={}"
                                    .format(version["git"].rstrip(".git"),
                                            version["ref"],
                                            package))
        else: # use master
            dependency_links.append("{}/tarball/master"
                                    .format(version["git"].rstrip(".git")))
    else:
        # install specific version or anthing above it
        install_requires.append("{}>={}".format(package, version))

setup(
    author="PurplePinapples",
    description="Generate and maintain an offline cache of anime and related databases",
    license="MIT",
    name='animeoffline',
    install_requires=install_requires,
    dependency_links=dependency_links,
    packages=find_packages(include=['animeoffline']),
    entry_points = {
        'console_scripts': [
            "anime_offline_mal = animeoffline.mal.mal:discover",
            "anime_offline_config = animeoffline.config:list_config"
        ]
    },
    version='0.1.0',
    include_package_data=True,
    zip_safe=False,
)
