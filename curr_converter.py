# -*- coding: utf-8 -*-

import json
import sys
from arguments import ArgumentParser
from currency_list import CurrencyList
from currency_rate import CurrencyRate
from database import Database
from database import Rate
from datetime import datetime, timedelta
from server import startServer

"""
Currency converter main file.
"""


def get_curr_symbol(symbol, curList):
    """
    Check if given symbol is currency symbol and turn it into code.
    """
    if curList.isCurrencyCode(symbol):
        return symbol
    else:
        return curList.getCodeBySymbol(symbol)


def exit_with_err(code, msg):
    """
    Print message to stderr and exit with error code.
    """
    sys.stdout.write(msg)
    sys.stdout.write('\n')
    sys.exit(code)


if __name__ == "__main__":
    startServer()
