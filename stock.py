import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
stock_data = []
i=0
def get_stock_price():
    driver.get('https://www.google.com/search?q=stock+price+of+tata+motors+history&oq=stock+price+of+tata+motors+history&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyCggHEAAYgAQYogQyBggIEC4YQNIBCDY4NzZqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8')

    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="IsqQVc NprOob wT3VGc"]'))
        )
        price = price_element.text
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        global stock_data
        stock_data.append(f'{price} at {current_time}')
        print("Current Stock Price:", price)
    except Exception as e:
        print("Error:", e)

try:
    while True and i<10:
        get_stock_price()

        time.sleep(10)
        i=i+1
except KeyboardInterrupt:
    print("Script stopped by user.")
finally:
    driver.quit()
    print(stock_data)
