from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name='annie_movie_recommendation',
    version='0.2',
    author='Joel',
    packages=find_packages(),
    install_requires=requirements,
)
