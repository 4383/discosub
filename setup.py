# -*- coding: utf-8 -*-
##################################################################################
#  /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$  #
# | $$__  $$|_  $$_/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$| $$__  $$ #
# | $$  \ $$  | $$  | $$  \__/| $$  \__/| $$  \ $$| $$  \__/| $$  | $$| $$  \ $$ #
# | $$  | $$  | $$  |  $$$$$$ | $$      | $$  | $$|  $$$$$$ | $$  | $$| $$$$$$$  #
# | $$  | $$  | $$   \____  $$| $$      | $$  | $$ \____  $$| $$  | $$| $$__  $$ #
# | $$  | $$  | $$   /$$  \ $$| $$    $$| $$  | $$ /$$  \ $$| $$  | $$| $$  \ $$ #
# | $$$$$$$/ /$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$/ #
# |_______/ |______/ \______/  \______/  \______/  \______/  \______/ |_______/  #
#                                                                                #
# discosub v0.2.0                                                                #
# author: 4383 (Hervé Beraud)                                                    #
# url: https://github.com/4383/discosub                                          #
##################################################################################
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'click',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='discosub',
    version='0.2.0',
    description="Simple, Faster, & Efficient, Subdomain Discovery Scanner",
    long_description=readme + '\n\n' + history,
    author="Hervé Beraud",
    author_email='herveberaud.pro@gmail.com',
    url='https://4383.github.io/discosub/',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests*', '__pycache__']
    ),
    package_dir={'discosub':'discosub'},
    entry_points={
        'console_scripts': [
            'discosub=discosub:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='discosub',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
