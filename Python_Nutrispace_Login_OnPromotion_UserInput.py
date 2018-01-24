# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys
from bs4 import BeautifulSoup
 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)  

def productInfoFound(infoText,productInfo):
    print(infoText + productInfo)
    # SAVE DATA to A FILE
    f = open("NutrispaceOnPromo_"+docTitle+".txt", "a")
    f.write(infoText + productInfo + "\n")
    f.close()
    
def productInfoNotFound(infoTextNF):
    print(infoTextNF)
    # SAVE DATA to A FILE
    f = open("NutrispaceOnPromo_"+docTitle+".txt", "a")
    f.write(infoTextNF + "\n")
    f.close()
 
def nutrispace_Login(base_url):
    driver.get(base_url + "/Nutrispace/Login.aspx")
    time.sleep(3)
    driver.find_element_by_id("p_lt_zoneLogin_NSLogonForm_UserName").clear()
	# Replace User Name with Real Data
    driver.find_element_by_id("p_lt_zoneLogin_NSLogonForm_UserName").send_keys("0000000")
    time.sleep(1)
    driver.find_element_by_id("p_lt_zoneLogin_NSLogonForm_Password").clear()
	# Replace User Password with Real Data
    driver.find_element_by_id("p_lt_zoneLogin_NSLogonForm_Password").send_keys("XYZXYZ")
    time.sleep(1)
    driver.find_element_by_id("p_lt_zoneLogin_NSLogonForm_LoginButton").click()
            
def get_dynamicOnPromotionProducts(docTitle):

    promoProducts = []   

    promoProducts = driver.find_elements_by_xpath('.//div[@class="boxGradient"]')
    #print(promoProducts)
    #print(len(promoProducts))
   
    if len(promoProducts) > 0:
        for elem in promoProducts: 
        # Promoted Product Titles and price
            try:
                #print (elem)
                title = elem.find_element_by_xpath(".//div[@class='highlightNorm']/div/h4/span").text
                infoText = "Promoted Product: "
                productInfo = title
                productInfoFound(infoText, productInfo)
            except: # catch *all* exceptions
                infoTextNF = "Couldn't retrieve this Promo Product Name."
                productInfoNotFound(infoTextNF)
            try:                        
                promo_price = elem.find_element_by_xpath(".//label[@class='promoPriceColor']").text
                infoText = "Promo Price: "
                productInfo = promo_price
                productInfoFound(infoText, productInfo)
            except: # catch *all* exceptions
                print("Couldn't retrieve Promo Product Price.")
            try:
                reg_price = elem.find_element_by_xpath(".//div[@class='linkBox']/span")
                if reg_price.text:
                    price = reg_price.text.split() 
                    infoText = "Regular Price: "
                    productInfo = price[0]
                    productInfoFound(infoText, productInfo)
            except: # catch *all* exceptions
                print("Couldn't retrieve Regular Product Price.")
            try:                        
                promo_description = elem.find_element_by_xpath(".//div[@class='productTxt']/div").text
                infoText = "Product Description: "
                productInfo = promo_description
                productInfoFound(infoText, productInfo)
            except: # catch *all* exceptions
                infoTextNF = "Couldn't retrieve this Promo Product Description."
                productInfoNotFound(infoTextNF)
            try:                        
                promo_code = elem.find_element_by_xpath(".//div[@class='linkBox']/strong").text
                print(promo_code)
                print("\n")
                f = open("NutrispaceOnPromo_"+docTitle+".txt", "a")
                f.write(promo_code + "\n"+"\n")
                f.close()
            except: # catch *all* exceptions
                print("Couldn't retrieve this Promo Code.")
                print("\n")
                # SAVE DATA to A FILE
                f = open("NutrispaceOnPromo_"+docTitle+".txt", "a")
                f.write("Couldn't retrieve this Promo Code" + "\n"+ "\n")
                f.close()
    else:
        print("No Products found on the Page")
        
def is_element_present(how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
    
def is_alert_present():
    try: driver.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True
    
def close_alert_and_get_its_text():
    try:
        alert = driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally: self.accept_next_alert = True
    
def tearDown():
    driver.quit()
    assertEqual([], self.verificationErrors)

docTitle = input("Enter the Month and Year, for the Output file: ")
driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "https://www.nutrimetics.co.nz/"
start_url = "https://www.nutrimetics.co.nz/Nutrispace/OD/Ordering/OnPromotion.aspx"
verificationErrors = []
accept_next_alert = True
# Start Login process
nutrispace_Login(base_url)
time.sleep(5)
# Navigate to the Product Promotions Start page
#gen_soup = get_OnPromotionWebpage(start_url)
driver.get(start_url)
time.sleep(8)
# Setup the continuous Scraping until there are no more Promo Product pages left to scrape
continue_scraping = True
while continue_scraping:
    # Navigate to the next Product Promotions page
    try:
        if driver.find_element_by_css_selector("#p_lt_zoneSlavePages_pageplaceholder1_p_lt_zoneContent_pageplaceholder_p_lt_zonebody_NSDataList_pager_LinkButtonLast").get_attribute('disabled'):
            start_url= None

    except:
            print("Couldn't find Last Page Link.")
            print("\n")
    else:
        try:
            driver.find_element_by_id("p_lt_zoneSlavePages_pageplaceholder1_p_lt_zoneContent_pageplaceholder_p_lt_zonebody_NSDataList_pager_LinkButtonNext").click()
            time.sleep(8)
        except:
            print("Couldn't find Next Page Link.")
            print("\n")

    # Dynamic Content needs to be loaded before you can then find elements with Selenium
    get_dynamicOnPromotionProducts(docTitle)
    if (start_url is None):
        #input("Press Enter to exit, and open the Product Promotion text file :")
        continue_scraping = False
        print("No More Promotion Pages to View")
        print("\n")
        print("Nutrispace webscraping has Finished. Open the Product Promotion text file.")

