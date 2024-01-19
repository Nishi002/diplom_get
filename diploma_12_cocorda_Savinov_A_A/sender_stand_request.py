# Савинов Андрей, 12-когорта - Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_orders(body):
    temp_dict = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                  json=body,
                  headers=data.headers).json()
    return temp_dict['track']

def get_orders(track):
    str_track = str(track)
    order = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH
                         + str_track,
                         headers=data.headers)
    return order