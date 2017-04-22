# -*- coding: utf-8 -*-

import argparse
from currency_list import CurrencyList
from currency_rate import CurrencyRate

"""
Static class compose arguments parser for currency converter.
"""


class ArgumentParser:

    @classmethod
    def getParser(cls):

        args_parser = argparse.ArgumentParser(
            prog="curr_converter",
            description='Currency converter - uses "' +
            CurrencyList.getUrl() + '" for currencies information and "' +
            CurrencyRate.getUrl() + '" for currency rates.'
        )

        args_parser.add_argument(
            '-a', '--amount',
            metavar='AMOUNT',
            type=float,
            required=True,
            help='Amount in given currency, that will be converted.'
        )

        args_parser.add_argument(
            '-i', '--input_currency',
            metavar='I_CURR',
            type=str,
            required=True,
            help='Input currency: 3-letter shortcut or currency symbol.'
        )

        args_parser.add_argument(
            '-o', '--output_currency',
            metavar='O_CURR',
            type=str,
            required=False,
            help='Output currency: 3-letter shortcut or currency symbol. ' +
            'If not listed, all currencies will be listed. ' +
            '(Unfortunately listing all currencies can take a bit longer, ' +
            'because we need to send each rate request individually).'
        )
        return args_parser
