from setuptools import setup

setup(name='pixLib',
      maintainer='Tony Butzer',
      maintainer_email='tonybutzer@gmail.com',
      version='1.0.0',
      description='Classes and Functions for et outputs netcdf first',
      packages=[
          'pixLib',
      ],
      install_requires=[
          'boto3',
      ],

)
