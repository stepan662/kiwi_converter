# -*- coding: utf-8 -*-

import argparse


class ArgumentParser:

    @classmethod
    def getParser(cls):

        args_parser = argparse.ArgumentParser(description='Currency converter.',
                                              formatter_class=argparse.RawTextHelpFormatter)

        args_parser.add_argument('-a', '--amount',
                                 metavar='AMOUNT',
                                 type=float,
                                 required=True,
                                 help='Amount in given currency, that will be converted.')

        args_parser.add_argument('-i', '--input_currency',
                                 metavar='I_CURR',
                                 type=str,
                                 required=True,
                                 help='Input currency: 3-letter shortcut or currency symbol.')

        args_parser.add_argument('-o', '--output_currency',
                                 metavar='O_CURR',
                                 type=str,
                                 required=False,
                                 help='Output currency: 3-letter shortcut or currency symbol.')
        return args_parser


if __name__ == "__main__":
    parser = ArgumentParser.getParser()
    print(parser.parse_args(u"-i CZK -o USD -a 10".split()))
