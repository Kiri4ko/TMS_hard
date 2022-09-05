import myhtml

from flask import Flask
from flask import Response
from flask import request
from requests import request as req
from pyowm import OWM
from pyowm.utils.config import get_default_config

app = Flask(__name__)


@app.route('/')
def hello_page():
    return Response(myhtml.home_page_buttons)


@app.route('/iam/', methods=['GET'])
def iam():
    return myhtml.iam_background


@app.route('/you/', methods=['GET'])
def you():
    return Response(f"<h4>user: {request.headers['User-Agent'], request.headers['Host']} </h4>")


@app.route('/weather/', methods=['GET', 'POST'])
def weather():
    return Response(myhtml.form_weather)


@app.route('/weather/city/', methods=['GET', 'POST'])
def weather_city():
    config_dict = get_default_config()
    config_dict['language'] = 'us'

    owm = OWM('YOUR API-key')
    mgr = owm.weather_manager()
    c = '\u00b0' + 'C'
    observation = mgr.weather_at_place(request.form.get('city'))
    weather = observation.weather
    temp_dict_celsius = weather.temperature('celsius')['temp']
    return Response(
        f"In the city of {request.form.get('city').capitalize()} now: {temp_dict_celsius} {c}, {weather.detailed_status}.")


@app.route('/currency-rate/', methods=['GET', 'POST'])
def exchange():
    return Response(myhtml.form_exchange)


@app.route('/currency-rate/currency-exchange/', methods=['GET', 'POST'])
def exchange_rate():
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={request.form.get('to_currency')}&" \
          f"from={request.form.get('from_currency')}&amount={request.form.get('amount')}"
    payload = {}
    headers = {
        "apikey": "YOUR API-key"
    }

    response = req('GET', url, headers=headers, data=payload)
    result = response.json()
    return Response(
        f"""Rate: {result['info']['rate']}<br>Result: {result['result']} {request.form.get('to_currency')}""")


if __name__ == '__main__':
    app.run()
