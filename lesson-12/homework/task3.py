import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  
driver.get("https://www.demoblaze.com/")


laptops_tab = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_tab.click()
time.sleep(3)  

laptop_data = []

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
  
    items = soup.find_all("div", class_="card")
    
    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        
        laptop_data.append({
            "name": name,
            "price": price,
            "description": description
        })
    
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)  
    except:
        break 


driver.quit()

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4, ensure_ascii=False)

print("Laptop data scraped and saved to laptops.json successfully!")
