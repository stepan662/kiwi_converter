# -*- coding: utf-8 -*-

import requests

class CurrencyList:

    _list_url = 'https://gist.githubusercontent.com/Fluidbyte/2973986/raw/b0d1722b04b0a737aade2ce6e055263625a0b435/Common-Currency.json'

    def __init__(self):
        resp = requests.get(self._list_url)
        if (resp.status_code != 200):
            resp.raise_for_status()

        self._list = resp.json()

    def getAllCurrencyCodes(self):
        codes = []
        for code in self._list:
            codes.append(code)
        return codes

    def getCodeBySymbol(self, symbol):
        for code in self._list:
            if(self._list[code][u"symbol"] == symbol):
                return code




if __name__ == "__main__":
    # check masic functionality
    list = CurrencyList()
    print(list.getAllCurrencyCodes())
    print(list.getCodeBySymbol(u"Kč"))
