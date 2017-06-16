#!/usr/bin/env python

from setuptools import setup

setup(name="feedo",
      version="1.0.0",
      description="Read, format and output an RSS stream.",
      url='https://github.com/kamikat/feedo',
      author="Kamikat",
      author_email="kamikat@banana.moe",
      install_requires=['feedparser'],
      packages=["feedo"],
      entry_points={
          'console_scripts': [ 'feedo = feedo:main' ] },
      license="MIT")
