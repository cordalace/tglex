"""Setuptools script."""

import codecs

import setuptools

with codecs.open('README.md', encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()

setuptools.setup(
    name='tglex',
    version="0.1.0",
    author='Azat Kurbanov',
    author_email='cordalace@gmail.com',
    description='Lexical analysis base for telegram bots',
    long_description=LONG_DESCRIPTION,
    license='MIT',
    url='https://github.com/cordalace/tglex',
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    entry_points={},
    package_data={
        'tglex': [],
    },
    zip_safe=True,
)
