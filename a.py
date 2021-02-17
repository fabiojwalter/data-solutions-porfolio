#!/usr/bin/env python3
"""
Documentation goes here...
"""

__author__ = "Fabio J. Walter"
__version__ = "0.1.0"
__license__ = "MIT"

import common.log
from logzero import logger

def run():
    """ Main entry point of the app """
    logger.info("hello world")
    logger.debug("outro teste")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    run()
