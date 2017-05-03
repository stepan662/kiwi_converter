from flask import make_response, jsonify, Flask, request
from currency_rate import CurrencyRate
from database import Database, Rate
from datetime import datetime, timedelta
import json

app = Flask(__name__)


@app.route('/rates', methods=['POST'])
def get_rates():
    data = request.get_json()

    if "from" not in data:
        return make_response(jsonify({'error': 'Missing from date'}))

    if "to" not in data:
        return make_response(jsonify({'error': 'Missing to date'}))

    if "curr" not in data:
        return make_response(jsonify({'error': 'Missing to curr (currency)'}))

    try:
        fromDate = datetime.strptime(data["from"], "%Y-%m-%d")
        toDate = datetime.strptime(data["to"], "%Y-%m-%d")
    except Exception as e:
        return make_response(jsonify({'error': 'Wrong date format'}), 404)

    interval = 1
    if "interval" in data:
        try:
            interval = int(data["interval"])
        except Exception as e:
            return make_response(jsonify({'error': 'Interval is not integer'}))

    currency = data["curr"]

    data = []
    if interval == 1:
        result = Database.getRates(fromDate, toDate, currency)
        for rate in result:
            data.append(rate.getDict())
    else:
        result = Database.getRates(fromDate, toDate, currency)
        for rate in result[::interval]:
            data.append(rate.getDict())

    return jsonify(data)


def startServer():
    app.run(debug=True)


if __name__ == '__main__':
    print(get_rates('2000', '2011', 'CZK'))
