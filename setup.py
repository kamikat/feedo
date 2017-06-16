#!/usr/bin/env python

from distutils.core import setup

setup(name="feedo",
      version="0.1dev",
      description="Read, format and output an RSS stream.",
      author="Kamikat",
      author_email="kamikat@banana.moe",
      packages=["feedo"],
      entry_points={
          'console_scripts': [ 'feedo = feedo:main' ] },
      license="MIT")
