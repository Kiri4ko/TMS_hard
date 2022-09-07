"""Parse data from with https://www.coingecko.com"""

from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel, Field
from requests import request
import json as JSON

app = FastAPI()


class Description(BaseModel):
    en: str


class Coin(BaseModel):
    id: str
    symbol: str
    name: str
    description: Description


@app.get("/")
def read_root():
    return {"Coins": "https://www.coingecko.com"}


"""Coin parse by name. """


@app.get("/coins/{coin_id}/")
def coin(coin_id: str):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
    response = request('GET', url).json()
    str_response = JSON.dumps(response)
    parse_response = Coin.parse_raw(str_response)
    return parse_response


"""Parse by name or id for all coins. """


@app.get("/coins/list/{id_name}/")
def list_coins_id(id_name: str):
    url = 'https://api.coingecko.com/api/v3/coins/list'
    response = request('GET', url).json()
    coin_name = [coin.get(id_name) for coin in response]
    return coin_name


"""Parse for all coins in a list."""


@app.get("/coins/all/list/")
def list_coins():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    response = request('GET', url).json()
    return response
