from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

from BaseTest.forgetpassword_locators import *


def test_forgetpassword1():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Forgetpassword).click()
    time.sleep(2)
    coupon = driver.find_element(By.ID, Forgetpassword_tab)
    coupon.clear()
    coupon.send_keys(Incorrect_email__send_key)
    time.sleep(7)
    driver.find_element(By.XPATH, Button).click()
    time.sleep(2)
    driver.close()


def test_forgetpassword2():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Forgetpassword).click()
    time.sleep(2)
    coupon = driver.find_element(By.ID, Forgetpassword_tab)
    coupon.clear()
    coupon.send_keys()
    time.sleep(7)
    driver.find_element(By.XPATH, Button).click()
    time.sleep(2)
    driver.close()

def test_forgetpassword3():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, Forgetpassword).click()
    time.sleep(2)
    coupon = driver.find_element(By.ID, Forgetpassword_tab)
    coupon.clear()
    coupon.send_keys(Email_send_key)
    time.sleep(7)
    driver.find_element(By.XPATH, Button).click()
    time.sleep(2)
    driver.close()