# -*- coding: utf-8 -*-

import argparse


class ArgumentParser:

    @classmethod
    def getParser(cls, cur_check):

        args_parser = argparse.ArgumentParser(description='Currency converter.',
                                              formatter_class=argparse.RawTextHelpFormatter)

        args_parser.add_argument('-a', '--amount',
                                 metavar='AMOUNT',
                                 type=float,
                                 required=True,
                                 help='Amount in given currency, that will be converted.')

        args_parser.add_argument('-i', '--input_currency',
                                 metavar='I_CURR',
                                 type=cur_check,
                                 required=True,
                                 help='Input currency: 3-letter shortcut or currency symbol.')

        args_parser.add_argument('-o', '--output_currency',
                                 metavar='O_CURR',
                                 type=cur_check,
                                 required=False,
                                 help='Output currency: 3-letter shortcut or currency symbol.')
        return args_parser


if __name__ == "__main__":
    def symbol_check(string):
        if len(string) == 3:
            return string.upper()
        raise argparse.ArgumentTypeError('"' + string + '" is not valid currency symbol')

    parser = ArgumentParser.getParser(symbol_check)
    print(parser.parse_args(u"-i CZK -o USD -a 10".split()))
