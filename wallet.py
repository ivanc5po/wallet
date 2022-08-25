import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
extension_path = "ether_metamask-10.18.3.xpi"
options = Options()
#options.add_argument('-headless')
options.add_argument('--disable-gpu')
driver=webdriver.Firefox(options=options)
driver.install_addon(extension_path, temporary=True)
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/div/button').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
time.sleep(1)
SECRET_RECOVERY_PHRASE = "XXXXXXXXXXXXXXXXXXXXXXXXX"
NEW_PASSWORD = "@@pupu9487"
time.sleep(1)
for i in range(12):
    inputs = driver.find_element("xpath", '//*[@id="import-srp__srp-word-'+str(i)+'"]').send_keys(SECRET_RECOVERY_PHRASE.split()[i])

driver.find_element("xpath", '//*[@id="password"]').send_keys(NEW_PASSWORD)
driver.find_element("xpath", '//*[@id="confirm-password"]').send_keys(NEW_PASSWORD)
driver.find_element("xpath", '//*[@id="create-new-vault__terms-checkbox"]').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/div[2]/form/button').click()
time.sleep(5)
driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/button').click()
time.sleep(2)
driver.find_element("xpath", '/html/body/div[2]/div/div/section/div[1]/div/button').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div/div/div[3]/div/div[3]/div[2]/a[2]').click()
time.sleep(1)
driver.find_element("xpath", '//*[@id="search-tokens"]').send_keys("USDC")
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/footer/button').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div[3]/footer/button[2]').click()
time.sleep(1)
print("餘額 USDC :", driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/span[2]').text)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div[1]/button[1]').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div/div/div/div[1]/button').click()
time.sleep(1)
driver.find_element("xpath", '/html/body/div[2]/div[2]/button[2]').click()
time.sleep(1)
driver.find_element("xpath", "/html/body/div[1]/div/span/div[1]/div/div/div").screenshot("screenshot.png")

img = Image.open("screenshot.png")
img.show()
