# -*- coding: utf-8 -*-

__author__ = 'Hervé Beraud'
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.2.0'

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
@click.option('--agressive', '-a', is_flag=True, help="Use agressive scanning mode (disabled by default)")
def run(agressive, **kwargs):
    '''Run a subdomain scanner on specified TARGET'''
    analyze(kwargs['target'], agressive)


@main.command()
def version():
    """Display Discosub Version"""
    print('discosub {version}'.format(version=__version__),)


if __name__ == "__main__":
    main()
