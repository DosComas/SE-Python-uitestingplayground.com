from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Crear la sesion de Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Acceder a la URL
driver.get('http://uitestingplayground.com/dynamictable')

# DO THINGS
headers = driver.find_elements(By.XPATH, '//span[@role="columnheader"]')
table = driver.find_elements(By.XPATH, '//span[@role="cell"]')

cpu_index = [header.text for header in headers].index('CPU')
cells = [cell.text for cell in table]
chrome_index = cells.index('Chrome')

yellow = driver.find_element(By.XPATH, '//*[@class="bg-warning"]').text

print(cells[chrome_index + cpu_index])
print(yellow.replace('Chrome CPU: ', ''))

assert yellow.replace('Chrome CPU: ', '') == cells[chrome_index + cpu_index]
print('Pass')

# Cerrar la sesion de Chrome
driver.quit()
