#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_discosub
----------------------------------

Tests for `discosub` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from discosub.main import main



class TestDiscosub(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert 'Fast BruteForce Subdomain Discover' in result.output
        help_result = runner.invoke(main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
