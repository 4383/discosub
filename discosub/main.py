# -*- coding: utf-8 -*-

__author__ = 'Hervé Beraud'
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.1.12'

import argparse
import sys
import click
from discosub.commands.discover import analyze


@click.group()
def main():
    """Fast BruteForce Subdomain Discover"""
    pass


@main.command()
@click.argument('target')
def run(**kwargs):
    '''Run a subdomain scanner on specified target'''
    analyze(kwargs['target'])


@main.command()
def version():
    """Display Discosub Version"""
    print('discosub {version}'.format(version=__version__),)


if __name__ == "__main__":
    main()
