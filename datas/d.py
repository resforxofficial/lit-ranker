from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# main_list = []
allof_list = []

with open("../dist/href.txt", "r", encoding="utf-8") as f:
    urls = f.read().splitlines()

for url in urls:
    driver.get(url)
    WebDriverWait(driver, 13).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div[3]/main/section/article[2]/div[3]'))
    )

    url_html = driver.page_source
    urlNew_html = BeautifulSoup(url_html, "html5lib")
    mainComment_div = urlNew_html.select_one("div.comment_wrap.show")

    with open("../dist/temp/orchmiest.html", "w", encoding="utf-8") as f:
        f.write(str(mainComment_div))