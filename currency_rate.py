# -*- coding: utf-8 -*-

import requests
import grequests
import currency_list

class CurrencyRate:

    _converter_url = 'http://rate-exchange-1.appspot.com/currency'


    @classmethod
    def _composeUrl(cls, src, target, amount):
        return cls._converter_url + "?from=" + src + "&to=" + target + "&q=" + str(amount)


    @classmethod
    def convert(cls, src, target, amount):
        resp = requests.get(cls._composeUrl(src, target, amount))
        if (resp.status_code != 200):
            resp.raise_for_status()

        return "{0:.2f}".format(resp.json()[u"v"])

    @classmethod
    def convertFromList(cls, src, targets, amount):
        rqsts = (grequests.get(cls._composeUrl(src, target, amount)) for target in targets)
        responses = grequests.map(rqsts)
        result = {}
        for resp in responses:
            if resp.status_code != 200:
                resp.raise_for_status()
            json = resp.json()
            result[json[u"to"]] = "{0:.2f}".format(json[u"v"])
        return result




if __name__ == "__main__":
    # check masic functionality
    print("USD:", CurrencyRate.convert("EUR", "USD", 10))
    codes = [
        "CZK",
        "USD",
    ]
    print(CurrencyRate.convertFromList("EUR", codes, 10))
