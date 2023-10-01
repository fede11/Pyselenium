import time
from selenium import webdriver
import pandas as pd

#Firefox
options = webdriver.FirefoxOptions()
options.set_preference("dom.webnotifications.serviceworker.enabled", False)
options.set_preference("dom.webnotifications.enabled", False)
options.add_argument('--headless')

driver = webdriver.Firefox(executable_path='D:py-selenium\geckodriver.exe',options=options)
driver.get('https://docs.google.com/forms/u/0/')

driver.find_element('xpath', '/html/body/div[4]/div[3]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]').click()

driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/span').click()

# Agregar elemento a formulario
driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/div/div[1]/div/span').click()
driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]').click()
driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]').click()
driver.find_element('xpath', '//*[@id="T2Ybvb4"]').send_keys('TEST')

df = pd.read_csv('username - username.csv')
print(df)

for row, datos in df.iterrows():
    print('Datos: ', datos)
    print('Datos keys: ', datos.keys())
    print('Row: ', row)
    username = datos['Username']
    identifier = datos['Identifier']
    firstName = datos['First name']
    lastName = datos['Last name']

    driver.get('https://forms.gle/ZFht7RL5f1rYwuCw9')

    time.sleep(3)

    driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(username)
    driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(identifier)
    driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(firstName)
    driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(lastName)
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

