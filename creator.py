import random
import string
import postalcodes as pc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Instance:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Linux; Android 5.1.1; SM-N950W Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.generated_accounts = {
            "count": 0,
            "emails": []
        }

    def generate(self, email, password):
        self.driver.get('https://www.uniqlo.com/ca/en/account/registry')
        try:
            # wait for email input to load, then begin filling form
            email_input = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div[3]/div/label/input')))
        except TimeoutException:
            return

        pass_input = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/form/div[4]/div/label/input')
        postal_input = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/form/div[5]/div/label/input')

        # accept terms box
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/form/div[13]/div').click()

        email_input.send_keys(email)
        pass_input.send_keys(password)
        postal_input.send_keys(self.gen_postal())

        # finalize form
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/form/div[16]/button').click()

        # wait for register button and click
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/button'))).click()
        except TimeoutException:
            print("[-] Error")
            return

        self.driver.delete_all_cookies()

        self.generated_accounts["count"] += 1
        self.generated_accounts["emails"].append(email)

    def gen_postal(self):
        postal_code = random.choice(pc.codes)
        for i in range(3):
            if i % 2 == 0:
                postal_code += random.choice("012345679")
            else:
                postal_code += random.choice(string.ascii_uppercase)
        return postal_code


i = Instance()
i.generate("abc@fpsnkrs.com", "123456789abc")
print(i.generated_accounts)
