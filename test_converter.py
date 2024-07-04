from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
chrome_options = Options()
options = [
  "--headless",
  "--window-size=1920,1200",
  "--no-sandbox",
]
for option in options:
  chrome_options.add_argument(option)




# se = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=se,options=chrome_options)

def test_error():
    url = "http://localhost/"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.get(url)
    driver.find_element(By.XPATH,"/html/body/div/div[4]/button").click()
    try:
        result_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "res"))
        )
        result = result_element.text
    except TimeoutException:
        print("timeout exception at test_error")
        exit(1)     
    try:
        assert result == "Error converting currency"
    except AssertionError:
        print("not correct error alert")
        exit(1)


def test_converter_1():
    url = "http://localhost/"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.get(url)
    driver.get(url)
    driver.find_element(By.CLASS_NAME,"search-amount-bar").send_keys("20")
    driver.find_element(By.XPATH,"/html/body/div/select[1]/option[64]").click()
    driver.find_element(By.XPATH,"/html/body/div/select[2]/option[149]").click()
    driver.find_element(By.CSS_SELECTOR, "div.conv > button.convert").click()
    try:
        result_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "res"))
        )
        result = result_element.text
    except TimeoutException:
        print("timeout exception at test_converter_1")
        exit(1)

    expected_result = "Converted Amount: 5.311576092"
    tolerance = 1  
    converted_amount = float(result.split(": ")[1])
    expected_amount = float(expected_result.split(": ")[1])
    try:
        assert abs(converted_amount - expected_amount) <= tolerance 
    except AssertionError:
        print("not the correct result")
        exit(1)

def test_converter_2():
    url = "http://localhost/"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.get(url)
    driver.get(url)
    driver.find_element(By.CLASS_NAME,"search-amount-bar").send_keys("1")
    driver.find_element(By.XPATH,"/html/body/div/select[1]/option[38]").click()
    driver.find_element(By.XPATH,"/html/body/div/select[2]/option[147]").click()
    driver.find_element(By.CSS_SELECTOR, "div.conv > button.convert").click()
    try:
        result_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "res"))
        )
        result = result_element.text
    except TimeoutException:
        print("timeout exception at test_converter_2")
        exit(1)

    expected_result = "Converted Amount: 1.7440912721"
    tolerance = 1  
    converted_amount = float(result.split(": ")[1])
    expected_amount = float(expected_result.split(": ")[1])
    try:
        assert abs(converted_amount - expected_amount) <= tolerance 
    except AssertionError:
        print("not the correct result")
        exit(1)

def test_quit():
    url = "http://localhost/"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.get(url)
    driver.quit()
	