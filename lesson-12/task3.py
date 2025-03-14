import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Initialize WebDriver (Ensure you have the correct path to your WebDriver)
driver = webdriver.Chrome()  # Update to Edge(), Firefox() if needed
driver.get("https://www.demoblaze.com/")

# Navigate to "Laptops" section
laptops_tab = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_tab.click()
time.sleep(3)  # Wait for the page to load

laptop_data = []

while True:
    # Parse the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Extract laptop details
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
    
    # Try to find the "Next" button and click it, else break loop
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)  # Wait for next page to load
    except:
        break  # No next button, exit loop

# Close the WebDriver
driver.quit()

# Save data to JSON file
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4, ensure_ascii=False)

print("Laptop data scraped and saved to laptops.json successfully!")
