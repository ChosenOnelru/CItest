from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://gisogd.gov.ru/'
NTD_name = 'Генераторы пены средней кратности. Технические условия'
NTD_correct_number = '50409-92'
NTD_incorrect_number = '50408-92'

def test_open_page(driver):
    driver.get(URL)
    assert 'gisogd' in driver.current_url

def test_find_NTD_by_correct_number(driver):
    driver.get(URL)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//a[contains(@href, "/rntd")]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Введите наименование или номер"]').send_keys(NTD_correct_number)
    driver.find_element(By.XPATH, '//button[contains(text(),"Найти")]').click()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
        (By.XPATH, '//div[contains(text(),"Найдено")]'), '1'))
    assert driver.find_element(By.XPATH, '//div[contains(text(),"Найдено")]').text == 'Найдено 1 документ'
    assert driver.find_element(By.XPATH, '//p[contains(text(),"Генераторы пены")]').text == f'{NTD_name}'
    driver.find_element(By.XPATH, '//button[contains(text(),"Сбросить")]').click()

def test_find_NTD_by_incorrect_number(driver):
    driver.get(URL)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//a[contains(@href, "/rntd")]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Введите наименование или номер"]').send_keys(NTD_incorrect_number)
    driver.find_element(By.XPATH, '//button[contains(text(),"Найти")]').click()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
        (By.XPATH, '//div[contains(text(),"Найдено")]'), '0'))
    assert driver.find_element(By.XPATH, '//div[contains(text(),"Найдено")]').text == 'Найдено 0 документов'
    driver.find_element(By.XPATH, '//button[contains(text(),"Сбросить")]').click()