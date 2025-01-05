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
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#container > section > article:nth-child(3) > div.view_content_wrap > header > div'))
    )

    url_html = driver.page_source
    urlNew_html = BeautifulSoup(url_html, "html5lib")
    main = urlNew_html.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div")
    # main_list.append(str(main))
    # mainListWrapString = joiner(main_list)

    title = main.select_one("h3 > span.title_subject").get_text()
    nick_name = main.select_one("div.gall_writer.ub-writer").get("data-nick")
    nick_id = main.select_one("div.gall_writer.ub-writer").get("data-uid")
    galldate = main.select_one("div > div.fl > span.gall_date").get("title")

    allof_data = {
        "title": title,
        "nick": nick_name,
        "id": nick_id,
        "date": galldate
    }
    allof_list.append(allof_data)
    allof_list = sorted(allof_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S"))

    with open("../dist/chr/allof.json", "w", encoding="utf-8") as f:
        json.dump(allof_list, f, indent=4, ensure_ascii=False)