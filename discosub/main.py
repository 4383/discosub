# -*- coding: utf-8 -*-

__author__ = 'Hervé Beraud'
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.1.0'

import argparse
import sys
from commands.discover import discover as cmd_discover
from core.ui import fail, splash

class DiscoSub(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
        description='Fast BruteForce Subdomain Discover',
        usage='''discosub <command> [<args>]

The most commonly used commands are:
    run     Run a subdomain scanner on specified target
        ''')
        epilogue='''Credits :

author: Hervé Beraud
version: 0.1.0
        '''.format(__version__)
        parser.add_argument('command', help='Sub command to run')
        parser.add_argument('--version',
            help='Print version',
            action='version',
            version='discosub {version}'.format(version=__version__))
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            fail('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()


    def run(self):
        cmd_discover()


def main(args=None):
    """Console script for microservice"""
    DiscoSub()


if __name__ == "__main__":
    main()
