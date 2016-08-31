# -*- coding: utf-8 -*-

import click
from discosub.main import main as mainstreet

@click.command()
def main(args=None):
    """Console script for discosub"""
    mainstreet()


if __name__ == "__main__":
    main()
