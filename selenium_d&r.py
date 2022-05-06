from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

browser.get("https://www.dr.com.tr/")
time.sleep(3)

#click best seller
cok_satanlar = browser.find_element_by_xpath("/html/body/div/header/div[4]/div[2]/ul[2]/li[1]/a")
cok_satanlar.click()
time.sleep(3)

#choose best seller with selecter
cok_satanlar_2 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/main/div[3]/div[3]/select/option[2]").click()

elements = browser.find_elements_by_css_selector(".prd-name")


#write a file 45 best seller books
f = open("best_seller_list.txt","w")
count = 1
for i in elements:
    f.write(str(count) +" - "+i.text+ "\n")
    count += 1


time.sleep(3)
browser.close()