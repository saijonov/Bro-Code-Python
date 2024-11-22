# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }
# html_text = requests.get(url, headers=headers)
# content = html_text.text
# soup = BeautifulSoup(content, "lxml")
# names = soup.find_all("div", class_="p13n-sc-truncate-desktop-type2  p13n-sc-truncated")
# prices = soup.find_all("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")
# for name, price in zip(names, prices):
#     print(f"{name.text} costs {price.text}")



# html_text = requests.get('https://www.grenache.be/en/shop').text
# soup = BeautifulSoup(html_text, 'lxml')
# place = soup.find("div", class_="o_wsale_products_grid_table_wrapper pt-3 pt-lg-0")
# names = place.find_all("a", class_="text-primary text-decoration-none")
# prices = place.find_all("span", class_="oe_currency_value")

# for name, price in zip(names, prices):
    
#     print(f"{name.text} costs {price.text}\n") 




# from selenium import webdriver

# # Set up Selenium WebDriver
# driver = webdriver.Chrome()  # or webdriver.Firefox()
# driver.get("https://uzum.uz/uz/category/elektronika-10020")

# # Let JavaScript load
# driver.implicitly_wait(10)  # Wait for dynamic content to load
# html = driver.page_source
# driver.quit()

# # Parse HTML with BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# ramka = soup.find("div", id="category-content")
# if ramka:
#     names = ramka.find_all("a", class_="product-card tap-noselect noselect is-vertical")
#     for name in names:
#         print(name.text.strip())
# else:
#     print("Category content not found.")






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from bs4 import BeautifulSoup
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://uzum.uz/uz/category/elektronika-10020")
# time.sleep(5)
# html_text = driver.page_source
# soup = BeautifulSoup(html_text, 'lxml')
# ramka = soup.find("div", id="category-content")

# if ramka:
#     print("Category content found.")
#     names = ramka.find_all("a", class_="product-card")
#     for name in names:
#         product_name = name.get('title') 
#         print(product_name)  
# else:
#     print("Category content not found.")
# driver.quit()






text = "apple, olma shaftoli"
print(text.split(","))





