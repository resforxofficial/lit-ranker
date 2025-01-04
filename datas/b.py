from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from util import joiner, startswith

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
href_list = []
temp = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

with open("../dist/marc.html", "r", encoding="utf-8") as f:
    fc = f.read()

mainSoup = BeautifulSoup(fc, "html5lib")
acont = mainSoup.find_all("a", { "view-msg": "" })
acont_text = mainSoup.find_all("a", { "view-msg": "" })
acontext_list = []

for act in acont_text:
    texts: str = act.get_text()
    if texts.strip() == "":
        pass
    elif texts.startswith("["):
        pass
    else:
        acontext_list.append(texts.strip())

actList = joiner(acontext_list)

for ac in acont:
    href = ac.get("href")
    href_list.append(href)

for hl in href_list:
    if hl == "None" or hl == None:
        pass

    elif startswith(hl, "http"):
        pass

    else:
        newhl = f"https://gall.dcinside.com{hl}"
        temp.append(newhl)

temphtml = joiner(temp)
with open("../dist/href.txt", "w", encoding="utf-8") as f:
    f.write(temphtml)

with open("../dist/chr/index.txt", "w", encoding="utf-8") as f:
    f.write(actList)

driver.quit()