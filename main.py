import requests
import datetime
import random
import string
import postalcodes as ps
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

catchall_domain = "fpsnkrs.com"


def generate():
    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Linux; Android 5.1.1; SM-N950W Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.uniqlo.com/ca/en/account/registry')

    bday = datetime.datetime.now() + datetime.timedelta(1) - relativedelta(years=17)

    email = gen_email(catchall_domain)
    password = '123@FPSnkrs'
    postal_code = gen_postal()
    dob = bday.strftime("%m%d%Y")

    email_input = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div/div/form/div[3]/div/label/input')
    pass_input = driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div/form/div[4]/div/label/input')
    postal_input = driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div/form/div[5]/div/label/input')
    dob_input = driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div/form/div[6]/div/label/input')
    driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div/form/div[13]/div/span/label').click()

    email_input.send_keys(email)
    pass_input.send_keys(password)
    postal_input.send_keys(postal_code)
    #dob_input.send_keys(dob)

    driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div/form/div[16]/button').click()

    driver.find_element_by_xpath(
        '//*[@id="accountApp"]/div/div/div[3]/div[2]/div/div[1]/button').click()

    input("a")
    return email


def gen_email(domain):
    if domain[0] == '@':
        pass
    else:
        domain = '@' + domain
    VOWELS = "aeiouAEIOU"
    CONSONANTS = "".join(set(string.ascii_lowercase +
                             string.ascii_uppercase) - set(VOWELS))
    word = ''
    for i in range(random.randint(5, 8)):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    generated_prefix = word + \
        str(random.choice("_35x9816.")) + str(random.randint(8, 99))
    return generated_prefix + domain


def gen_postal():
    postal_code = random.choice(ps.ps_codes)
    for i in range(3):
        if i % 2 == 0:
            postal_code += random.choice("012345679")
        else:
            postal_code += random.choice(string.ascii_uppercase)
    return postal_code


generate()
