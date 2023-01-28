from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from PIL import Image
from pytesseract import pytesseract
import os
import time

class ScraperBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        with open('data.json', 'r') as fp:
            self.bot_data = json.load(fp)
     
    def __selectElementXPATH(self, xpath: str, toBeClicked: bool, driver, input_key: str = "") -> None:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        el = driver.find_element(By.XPATH, xpath)
        if input_key != "":
            el.send_keys(input_key)
            toBeClicked = False
        if toBeClicked:
            el.click()

    def BrokeCaptcha(self):
        self.driver.get(self.bot_data['init_url'])
        while 1:
            self.captcha_img = self.driver.find_element(By.XPATH, self.bot_data['captcha_img'])
            self.captcha_img.screenshot("images/captcha.png")
            path_to_tesseract = r'C:\Users\Lakal\Documents\Decebtral\CaptchaScraper\Tesseract\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = path_to_tesseract
            path_to_image = 'images/captcha.png'
            img = Image.open(path_to_image)
            text = pytesseract.image_to_string(img)
            time.sleep(2)  # You can skip this. I add this time to show exactly
            self.__selectElementXPATH(xpath = self.bot_data['input_code'], toBeClicked = False, driver = self.driver, input_key=text)
            time.sleep(2)  # You can skip this. I add this time to show exactly
            self.__selectElementXPATH(xpath = self.bot_data['btn_submit'], toBeClicked = True, driver=self.driver)
            time.sleep(5)  # You can skip this. I add this time to show exactly
            x = self.driver.current_url
            print(x)
            if x != 'http://localhost:8000/':
                print("Success solve the captcha!")
                break





if __name__ == '__main__':
    bot = ScraperBot()
    bot.BrokeCaptcha()