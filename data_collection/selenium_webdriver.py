from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


chrome_driver_path='.\chromedriver.exe'

def fetch_dealerlist_webscraping(webdriver_path: str, url: str, search_term) -> pd.DataFrame():

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.title
    #search_term="Toronto,ON"
    ele=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/input[1]')
    ele.send_keys(search_term)
    try:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[4]/div[5]/button').click()
        

        
        #for i in range(0,5):
        #    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
        #    time.sleep(1)

        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
        time.sleep(1)
        #time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
        time.sleep(1)
        #time.sleep(2)
        #driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
        #time.sleep(1)
        #driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[5]/div[2]/div/div/button').click()
    except:
        print("Button does not exists")
    dealer_names = driver.find_elements(By.CLASS_NAME   ,"dealer-name")
    distance = driver.find_elements(By.CLASS_NAME   ,"distance")
    address = driver.find_elements(By.CLASS_NAME   ,"address")
    print(type(address))
    dealer_list=[]
    distance_list =[]
    address_list =[]
    dealer_info_dict={}
    for el1 in dealer_names:
        dealer_list.append(el1.text)
        print(len(dealer_list))
    for el2 in distance:
        if el2.text:
            print(el2.text)
            distance_list.append(el2.text)
            print(len(distance_list))
    
    for el3 in address.__iter__():
        if el3.text:
            print(type(el3.text))
            print(el3.text)
            print(el3.text[1])
            address_list.append(el3.text)
            print(len(address_list))
    
    dealer_info_dict = { "Dealer_Name": dealer_list, "Distance": distance_list, "Address": address_list}
    df = pd.DataFrame(dealer_info_dict)
    return df


