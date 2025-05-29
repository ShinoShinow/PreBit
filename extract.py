from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys

# PROXY = "127.0.0.1:12334"
# Chorme_Options = webdriver.ChromeOptions()
# Chorme_Options.add_argument(f'--proxy-server={PROXY}')

service = Service("chromedriver.exe")

driver = webdriver.Chrome(service=service)#, options=Chorme_Options)

driver.get("https://www.investing.com/search/?q=bitcoin&tab=news")


# accept_cookies = WebDriverWait(driver, 100).until(
#     EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
# )
# accept_cookies.click()

close_popup = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))    
)
close_popup.click()

href_elements = driver.find_elements(By.XPATH, '//div[@class="articleItem"]/preceding::a')

hrefs = [a.get_attribute('href') for a in href_elements if a.get_attribute('href')]

driver.close()


