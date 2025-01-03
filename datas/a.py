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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def generatorCrawl(end_page: int):
    allTrHtml = ""

    for i in range(end_page, 0, -1):
        try:
            driver.get(f"https://gall.dcinside.com/mgallery/board/lists/?id=illit&page={i}")
            
        except Exception as e:
            print(str(e))

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody'))
            )

            html = driver.page_source
            soup = BeautifulSoup(html, "html5lib")
            tbody = soup.find_all("tbody", { "class": "listwrap2" })

            for tb in tbody:
                tr = tb.find_all("tr", { "class": "ub-content us-post" })
                trhtml = joiner(tr)
                allTrHtml += trhtml + "\n"

        except Exception as e:
            print(str(e))
            
    with open("../dist/marc.html", "w", encoding="utf-8") as f:
        f.write(allTrHtml)
        f.close()
    
    driver.quit()

generatorCrawl(8)