import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime

test_email = 'chosenonex1@gmail.com'
test_password = 'gNrts5W?K_.qLFu'
API_key = '2c254a2efb0b9008ce295e94a0939a2f'
cities = ['Moscow', 'Paris']
URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url