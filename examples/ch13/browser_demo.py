from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

# 使用内存 HTML，先核对定位与等待。
html = '<p id="status">ready</p>'
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
with webdriver.Chrome(options=options) as browser:
    browser.get("data:text/html," + quote(html))
    element = WebDriverWait(browser, 5).until(
        conditions.visibility_of_element_located((By.ID, "status"))
    )
    print(element.text)
