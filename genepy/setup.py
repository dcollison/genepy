#!/usr/bin/env python

from distutils.core import setup

setup(name='genepy',
      version='0.1',
      description='Genetic Algorithm Library',
      author='Dale Collison',
      author_email='dale.a.collison@gmail.com',
      url='https://github.com/dcollison/genepy',
      packages=['genepy',
                'genepy.brain',
                'genepy.defaults',
                'genepy.genetic_algorithm',
                'genepy.organism',
                'genepy.population'],
      )
