"""Setuptools script."""

import codecs

import setuptools

with codecs.open('README.md', encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()

setuptools.setup(
    name='tglex',
    version='0.2.0',
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
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Communications :: Chat',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Typing :: Typed',
    ],
)
