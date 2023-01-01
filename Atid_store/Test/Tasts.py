from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from Atid_store.BaseTest.Locatores import *
import  pytest

def test_store():
    driver = webdriver.Chrome()
    driver.get(Website_store)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Store).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Product_Store).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Store_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Cart_cheak_store).click()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Store_coupon)
    coupon.clear()
    coupon.send_keys(Coupon_send_keys_store)
    time.sleep(2)
    driver.find_element(By.XPATH, Coupone_button_store).click()
    time.sleep(5)
    product_name = driver.find_element(By.XPATH, Productname_store).text
    assert product_name == "Basic Gray Jeans"
    driver.close()


def test_men():
    driver = webdriver.Chrome()
    driver.get(Website_men)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Men).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Product_men).click()
    time.sleep(2)
    driver.find_element(By.XPATH, men_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Cart_cheak_men).click()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, men_coupon)
    coupon.clear()
    coupon.send_keys(Coupon_send_keys_men)
    time.sleep(2)
    driver.find_element(By.XPATH, Coupone_button_men).click()
    time.sleep(5)
    product_name = driver.find_element(By.XPATH, Productname_men).text
    assert product_name == "Black Hoodie"
    driver.close()


def test_women():
    driver = webdriver.Chrome()
    driver.get(Website_Women)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Women).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Product_Women).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Women_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Cart_cheak_Women).click()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Women_coupon)
    coupon.clear()
    coupon.send_keys(Coupon_send_keys_Women)
    time.sleep(2)
    driver.find_element(By.XPATH, Coupone_button_Women).click()
    time.sleep(5)
    product_name = driver.find_element(By.XPATH, Productname_Women).text
    assert product_name == "Bright Red Bag"
    driver.close()


def test_accessosories():
    driver = webdriver.Chrome()
    driver.get(Website_accessosories)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Accessosories).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Product_accessosories).click()
    time.sleep(2)
    driver.find_element(By.XPATH, accessosories_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Cart_cheak_accessosories).click()
    coupon = driver.find_element(By.NAME, accessosories_coupon)
    coupon.clear()
    coupon.send_keys(Coupon_send_keys_accessosories)
    time.sleep(2)
    driver.find_element(By.XPATH, Coupone_button_accessosories).click()
    time.sleep(5)
    product_name = driver.find_element(By.XPATH, Productname_accessosories).text
    assert product_name == "Buddha Bracelet"
    driver.close()