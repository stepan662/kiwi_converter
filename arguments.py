# -*- coding: utf-8 -*-

import argparse;

currency_symbols = {
    u'$':  u'USD',   # US Dollar
    u'€':  u'EUR',   # Euro
    u'₡':  u'CRC',   # Costa Rican Colón
    u'£':  u'GBP',   # British Pound Sterling
    u'₪':  u'ILS',   # Israeli New Sheqel
    u'₹':  u'INR',   # Indian Rupee
    u'¥':  u'JPY',   # Japanese Yen
    u'₩':  u'KRW',   # South Korean Won
    u'₦':  u'NGN',   # Nigerian Naira
    u'₱':  u'PHP',   # Philippine Peso
    u'zł': u'PLN',   # Polish Zloty
    u'₲':  u'PYG',   # Paraguayan Guarani
    u'฿':  u'THB',   # Thai Baht
    u'₴':  u'UAH',   # Ukrainian Hryvnia
    u'₫':  u'VND',   # Vietnamese Dong
}

def symbol_check(string):
    if len(string) == 3:
        return string.upper()
    elif string in currency_symbols:
        return currency_symbols[string]
    raise argparse.ArgumentTypeError('"' + string + '" is not valid currency symbol')

args_parser = argparse.ArgumentParser(description='Currency converter.',
                                 formatter_class=argparse.RawTextHelpFormatter)

args_parser.add_argument('-a', '--amount',
                    metavar='AMOUNT',
                    type=float,
                    required=True,
                    help='Amount in given currency, that will be converted.')

args_parser.add_argument('-i', '--input_currency',
                    metavar='I_CURR',
                    type=symbol_check,
                    required=True,
                    help='Input currency: 3-letter shortcut or currency symbol.')

args_parser.add_argument('-o', '--output_currency',
                    metavar='O_CURR',
                    type=symbol_check,
                    required=False,
                    help='Output currency: 3-letter shortcut or currency symbol.')
