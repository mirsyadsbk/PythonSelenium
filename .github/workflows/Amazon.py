from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import traceback

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web=webdriver.Chrome('C:\chromedriver')
web.get('https://www.amazon.com')
assert "Amazon" in web.title

link=web.find_element(by=By.ID, value="nav-hamburger-menu")
link.click()
time.sleep(3)

shop=web.find_element(by=By.LINK_TEXT, value="Electronics")
shop.click()
time.sleep(2)

ele=web.find_element(by=By.LINK_TEXT, value="Television & Video")
ele.click()
time.sleep(2)

tv=web.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[2]/ul/li[12]/span")
tv.click()
time.sleep(3)

size=web.find_element(by=By.LINK_TEXT, value="32 Inches & Under")
size.click()
time.sleep(4)

sort=web.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span/span")
sort.click()
time.sleep(3)

desc=web.find_element(by=By.ID, value="s-result-sort-select_2")
desc.click()
time.sleep(4)

price=web.find_element(by=By.ID, value="high-price")
try:
    price.send_keys("150")
    assert "150" in price.text
except AssertionError:
    print(traceback.format_exc())
time.sleep(4)
price.send_keys(Keys.ENTER)
time.sleep(6)

year=web.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[2]/li[4]/span/a/div")
year.click()
time.sleep(5)

product=web.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[4]/div[1]/h2/a/span")
product.click()
time.sleep(5)

add=web.find_element(by=By.NAME , value="submit.add-to-registry.wishlist.unrecognized")
add.click()
time.sleep(4)

login=web.find_element(by=By.NAME, value="email")
login.send_keys("Irsyad")
print(login.is_displayed)   
time.sleep(3)
login.send_keys(Keys.ENTER)
time.sleep(6)

web.close()
