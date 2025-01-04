from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from util import joiner

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

with open("../dist/href.txt", "r", encoding="utf-8") as f:
    urls = f.read().splitlines()

for url in urls:
    driver.get(url)
    WebDriverWait(driver, 13).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#container > section > article:nth-child(3) > div.view_content_wrap > header > div'))
    )

    url_html = driver.page_source
    urlNew_html = BeautifulSoup(url_html, "html5lib")
    main = urlNew_html.find("main", attrs={"class": "clear minor_view"})
    header_want = main.find("div", attrs={"class": "view"})