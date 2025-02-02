from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 웹 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 페이지 열기
driver.get("https://weverse.io")

# 버튼이 클릭 가능할 때까지 기다리기
wait = WebDriverWait(driver, 10)  # 최대 10초 대기
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal > div.BaseModalView_button_container__IHoFw > div:nth-child(2) > button")))

# 버튼 클릭
button.click()

# 페이지가 완전히 로드될 때까지 잠시 기다리기
driver.implicitly_wait(5)

# 추가 작업 (예: 로그인 등)
button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div.App > div > div.GlobalLayoutView_header__1UkFL > header > div > div.HeaderView_action__QDUUD > button")))
button2.click()

tex = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.sc-460609bf-2.hmieKE > h1")
print(tex.text)

inp = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.sc-460609bf-2.hmieKE > form > div > div.sc-3bde3d5b-9.dPngoK > input")
inp.send_keys("fd17torich@gmail.com")

button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div.sc-460609bf-2.hmieKE > div > button")))
button3.click()

inp2 = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.sc-460609bf-2.hmieKE > div > form > div.sc-d0f94a43-0.bCrkf > div > div.sc-3bde3d5b-9.dPngoK > input")
inp2.send_keys("wi;Qi+MGw8FM,#@")

driver.implicitly_wait(5)

button4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div.sc-460609bf-2.hmieKE > div > form > div.sc-3f5b46e7-0.ewkQvY > button")))
button.click()

# 브라우저 종료
# driver.quit()
