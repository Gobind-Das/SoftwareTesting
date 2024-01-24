# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:35:34 2024

@author: user
"""

# Required Python Packages:
# - selenium
# - beautifulsoup4
# - pdfkit
# pip install selenium beautifulsoup4 pdfkit

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pdfkit

# Function to initialize and configure the Edge webdriver
def configure_webdriver():
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    return webdriver.Edge(options=options)

# Function to perform the login
def perform_login(driver, username, password):
    try:
        driver.get("https://eapplication.nitrkl.ac.in/nitris/Login.aspx")

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUserName"))
        )
        password_field = driver.find_element(By.ID, "txtPassword")

        username_field.send_keys(username)
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.title_contains("Your Expected Title on Successful Login")
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        if "Your Expected Text on Successful Login" in soup.get_text():
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")

def result(driver):
    try:
        driver.get("https://eapplication.nitrkl.ac.in/nitris/Student/Examination/Results/Internal/Grade_Card_PG.aspx/?guttr^^**324432JHGFD67=MzQwMTg%3d-ymNx7mmdtRE%3d")
        
        time.sleep(5)

        # Perform any other actions or extractions needed from the result page

        # Save the page as an HTML file
        with open("result_page.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        # Save the page as a PDF file
        pdf_path = "result_page.pdf"
        driver.find_element(By.XPATH, '//body').screenshot(pdf_path)
        
        # Alternatively, use pdfkit to save the page as a PDF
        # pdfkit.from_url("https://eapplication.nitrkl.ac.in/nitris/Student/Examination/Results/Internal/Grade_Card_PG.aspx/?guttr^^**324432JHGFD67=MzQwMTg%3d-ymNx7mmdtRE%3d", pdf_path)

        print(f"Result saved as HTML: result_page.html")
        print(f"Result saved as PDF: {pdf_path}")

    except Exception as e:
        print(f"An error occurred in result function: {e}")

def main():
    username = '223CS3144'
    password = '#############'
    driver = None

    try:
        driver = configure_webdriver()
        perform_login(driver, username, password)
        result(driver)

    finally:
        if driver is not None:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    main()
