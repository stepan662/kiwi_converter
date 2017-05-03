# -*- coding: utf-8 -*-

import requests
import grequests
import currency_list
from datetime import datetime

"""
Static class wrapping online currency converter api.
"""


class CurrencyRate:

    _converter_url = 'http://api.fixer.io/'

    @classmethod
    def getUrl(cls):
        """
        Static class method returning url of remote json file.
        """
        return cls._converter_url

    @classmethod
    def _composeUrl(cls, src, date="latest"):
        """
        Private class method, compose url from given parameters.
        """
        return cls._converter_url +\
            date + "?base=" + src

    @classmethod
    def getRatesInDate(cls, date):
        resp = requests.get(cls._composeUrl("EUR", date))
        if (resp.status_code != 200):
            resp.raise_for_status()
        return resp.json()["rates"]


if __name__ == "__main__":
    dates = []
    for year in range(2000, 2017):
        date = datetime.strptime(str(year), "%Y")
        dates.append(date.strftime("%Y-%m-%d"))
    for k in CurrencyRate.getRatesInDates(dates):
        print(k)
