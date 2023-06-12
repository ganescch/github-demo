from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(executable_path="/home/ganesch/Downloads/chromedriver/chromedriver")

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
driver.close()