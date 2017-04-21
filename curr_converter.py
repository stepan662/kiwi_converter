# -*- coding: utf-8 -*-

import requests
import json
import sys
from arguments import ArgumentParser
from currency_list import CurrencyList

def get_currency_symbol(symbol, curList):
    if curList.isCurrencyCode(symbol):
        return symbol
    else:
        return curList.getCodeBySymbol(symbol)

def main(argv):
    argParser = ArgumentParser.getParser()
    args = argParser.parse_args(argv)

    moneyAmount = args.amount

    # init currency list - contains all symbols and codes
    currencyList = CurrencyList()

    # get currency code either from curency symbol
    try:
        inCurrency = get_currency_symbol(args.input_currency, currencyList)
    except ValueError as e:
        sys.exit("Input currency error: " + str(e))


    if args.output_currency:
        # output currency is defined - get just one rate
        outCurrency = get_currency_symbol(args.output_currency, currencyList)
        print("get rate from " + inCurrency + " to " + outCurrency)



    else:
        # no output currency - get all rates
        print("get all rates")







if __name__ == "__main__":
    main("-i Kč -a 10".split())
