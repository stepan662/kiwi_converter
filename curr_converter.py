# -*- coding: utf-8 -*-

import requests
import json
import sys
from arguments import ArgumentParser
from currency_list import CurrencyList
from currency_rate import CurrencyRate

def get_currency_symbol(symbol, curList):
    symbol = unicode(symbol, "utf-8")
    if curList.isCurrencyCode(symbol):
        return symbol
    else:
        return curList.getCodeBySymbol(symbol)

def main(argv):
    argParser = ArgumentParser.getParser()
    args = argParser.parse_args(argv)


    # init currency list - contains all symbols and codes
    try:
        currencyList = CurrencyList()
    except Exception as e:
        sys.exit("CurrencyList Error: " + str(e))

    # get currency code either from curency symbol
    try:
        inCurrency = get_currency_symbol(args.input_currency, currencyList)
    except ValueError as e:
        sys.exit("Input currency error: " + str(e))

    moneyAmount = args.amount

    # prepare input json
    inputDict = {
        "amount": "{0:.2f}".format(args.amount),
        "currency": inCurrency
    }

    # prepare output json
    outputDict = {

    }

    if args.output_currency:
        # output currency is defined - get just one rate
        try:
            outCurrency = get_currency_symbol(args.output_currency, currencyList)
        except ValueError as e:
            sys.exit("Output currency error: " + str(e))

        try:
            outputDict[outCurrency] = CurrencyRate.convert(inCurrency, outCurrency, moneyAmount)
        except Exception as e:
            sys.exit("Currency converter error: " + str(e))



    else:
        # no output currency - get all rates
        all_currencies = currencyList.getAllCurrencyCodes()
        try:
            outputDict = CurrencyRate.convertFromList(inCurrency, all_currencies, moneyAmount)
        except Exception as e:
            sys.exit("Currency converter error: " + str(e))




    # organize into json format
    output = json.dumps({
        "input": inputDict,
        "output": outputDict
    }, sort_keys=True, indent=4, separators=(',', ': '))

    print(output)


if __name__ == "__main__":
    main(sys.argv[1:])
