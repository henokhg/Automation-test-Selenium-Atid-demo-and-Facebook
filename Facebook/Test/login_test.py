from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from BaseTest.login_locators import *
import pytest

def test_login_1():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Email)
    coupon.clear()
    coupon.send_keys(Email_send_key1)
    time.sleep(7)
    coupon = driver.find_element(By.NAME, Pass)
    coupon.clear()
    coupon.send_keys(Pass_send_key1)
    time.sleep(5)
    driver.find_element(By.XPATH, Login).click()
    time.sleep(5)
    driver.close()


def test_login_2():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Email)
    coupon.clear()
    coupon.send_keys(Email_send_key1)
    time.sleep(7)
    driver.find_element(By.XPATH, Login).click()
    time.sleep(5)
    driver.close()


def test_login_3():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Email)
    coupon.clear()
    coupon.send_keys(Email_send_key2)
    time.sleep(7)
    coupon = driver.find_element(By.ID, Pass)
    coupon.clear()
    coupon.send_keys(Pass_send_key2)
    time.sleep(5)
    driver.find_element(By.XPATH, Login).click()
    time.sleep(5)
    driver.close()


def test_login_4():
    driver = webdriver.Chrome()
    driver.get(Website)
    driver.maximize_window()
    time.sleep(2)
    coupon = driver.find_element(By.NAME, Email)
    coupon.clear()
    coupon.send_keys()
    time.sleep(1)
    coupon = driver.find_element(By.ID, Pass)
    coupon.clear()
    coupon.send_keys()
    time.sleep(1)
    driver.find_element(By.XPATH, Login).click()
    time.sleep(5)
    driver.close()




