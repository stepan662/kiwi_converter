from currency_list import CurrencyList
from currency_rate import CurrencyRate
from database import Database
from database import Rate
from datetime import datetime, timedelta
import time


def fillDatabase():
    """
    Get currency history.
    """

    dates = []
    date = datetime(2000, 1, 1, 1)
    endDate = datetime.now()
    while date <= endDate:
        dates.append(date)
        date += timedelta(1)

    Database.init()

    for date in dates:
        rateList = []
        dateString = date.strftime("%Y-%m-%d")
        time.sleep(0.01)
        rates = CurrencyRate.getRatesInDate(dateString)
        for currency in rates:
            rateList.append(Rate(
                date,
                currency,
                rates[currency]
                ))
        print(dates.index(date), len(dates))
        Database.insert(rateList)


if __name__ == "__main__":
    fillDatabase()
