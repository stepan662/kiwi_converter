# -*- coding: utf-8 -*-

import requests

"""
Class wrapping currencies detail list.
"""


class CurrencyList:

    _list_url = 'https://gist.githubusercontent.com/Fluidbyte/2973986/' +\
        'raw/b0d1722b04b0a737aade2ce6e055263625a0b435/Common-Currency.json'

    @classmethod
    def getUrl(cls):
        """
        Static class method returning url of remote json file.
        """
        return cls._list_url

    def __init__(self):
        """
        Download data on init.
        Throws exception in case of network or api error.
        """
        resp = requests.get(self._list_url)
        if (resp.status_code != 200):
            resp.raise_for_status()

        self._list = resp.json()

    def getAllCurrencyCodes(self):
        """
        Returns array of all known currencies codes (USD, EUR, ...).
        """
        codes = []
        for code in self._list:
            codes.append(code)
        return codes

    def getCodeBySymbol(self, symbol):
        """
        Returns currency code by given symbol ($ -> USD, Kč -> CZK),
        Raise exception, when symbol is not found.
        """
        for code in self._list:
            if(self._list[code]["symbol"] == symbol):
                return code
        raise ValueError(symbol + " is not currency symbol")

    def isCurrencyCode(self, code):
        """
        Check if currency code does exist.
        """
        return code in self._list


if __name__ == "__main__":
    clist = CurrencyList()
    print(len(clist.getAllCurrencyCodes()))
