# -*- coding: utf-8 -*-

import requests
import grequests
import currency_list

"""
Static class wrapping online currency converter api.
"""


class CurrencyRate:

    _converter_url = 'http://rate-exchange-1.appspot.com/currency'

    @classmethod
    def getUrl(cls):
        """
        Static class method returning url of remote json file.
        """
        return cls._converter_url

    @classmethod
    def _composeUrl(cls, src, target, amount):
        """
        Private class method, compose url from given parameters.
        """
        return cls._converter_url +\
            "?from=" + src + "&to=" + target + "&q=" + str(amount)

    @classmethod
    def convert(cls, src, target, amount):
        """
        Class method, converts given amount of money from src currency to
        target currency. If currency codes are not valid or
        there is network error, raise exception.
        Returns currency code with converted amount in dictionary structure.
        """
        resp = requests.get(cls._composeUrl(src, target, amount))
        if (resp.status_code != 200):
            resp.raise_for_status()

        return "{0:.2f}".format(resp.json()["v"])

    @classmethod
    def convertFromList(cls, src, targets, amount):
        """
        Class method, converts given amount of money from src currency all
        given currencies. Sends request for each currency asynchronously.
        If codes are invalid or there is network error, raise exception.
        Returns currency codes with converted amounts in dictionary structure.
        """
        rqsts = (grequests.get(
            cls._composeUrl(src, target, amount)) for target in targets)

        responses = grequests.map(rqsts)
        result = {}
        for resp in responses:
            if resp.status_code != 200:
                resp.raise_for_status()
            json = resp.json()
            result[json["to"]] = "{0:.2f}".format(json["v"])
        return result
