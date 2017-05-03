from currency_rate import CurrencyRate
from database import Database
from database import Rate
from datetime import datetime, timedelta
import time
import sys


def fillDatabase():
    """
    Get currency history.
    """

    dates = []
    date = datetime(2000, 1, 1, 1)

    lastRecord = Database.getLastRow()
    if len(lastRecord) == 1:
        date = lastRecord[0].date

    today = datetime.now().replace(minute=0, hour=0, second=0, microsecond=0)
    while date <= today:
        dates.append(date)
        date += timedelta(1)

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

        sys.stdout.write("\rDownloading last rates: " +
                         str(dates.index(date)) +
                         "/" + str(len(dates)))
        Database.insert(rateList)


if __name__ == "__main__":
    fillDatabase()
