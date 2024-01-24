# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:35:34 2024

@author: user
"""


# Required Python Packages:
# - selenium
# - beautifulsoup4
#pip install selenium beautifulsoup4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Function to initialize and configure the Edge webdriver
def configure_webdriver():
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    # options.add_argument('--headless')  # Run Edge in headless mode
    return webdriver.Edge(options=options)

# Function to perform the login
def perform_login(driver, username, password):
    try:
        # Open the NIT Rourkela login
        driver.get("https://eapplication.nitrkl.ac.in/nitris/Login.aspx")

        # Find the username and password input fields
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUserName"))
        )
        password_field = driver.find_element(By.ID, "txtPassword")
        
        
        # password_field = driver.find_element_by_id("LoginUserPassword_auth_password")

        # Input the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to complete
        WebDriverWait(driver, 10).until(
            EC.title_contains("Your Expected Title on Successful Login")
        )

        # Check if the login was successful using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        if "Your Expected Text on Successful Login" in soup.get_text():
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")



def result(driver):
   
    #academic_field = driver.find_element(By.ID, "Academic")
    #driver.get("https://eapplication.nitrkl.ac.in/nitris/Student/Default.aspx?AppID=Ng%3d%3d-dYSTlPCIpzE%3d&AppName=RXhhbWluYXRpb24%3d-%2fdxDr14tNrU%3d")
    driver.get("https://eapplication.nitrkl.ac.in/nitris/Student/Examination/Results/Internal/Grade_Card_PG.aspx/?guttr^^**324432JHGFD67=MzQwMTg%3d-ymNx7mmdtRE%3d")
    #academic_field.click()
    time.sleep(2)
    
        # Save the page as an HTML file
    html_file_path = r"C:\SoftwareTestingLab\Day3\classroom\result_page1.html"
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    
    # Save the page as a PDF file
    #pdf_path = r"C:\SoftwareTestingLab\Day3\classroom\result_page1.pdf"
    #driver.find_element(By.XPATH, '//body').screenshot(pdf_path)
    
    print(f"Result saved as HTML: {html_file_path}")
    #print(f"Result saved as PDF: {pdf_path}")


    
    


    
# Main function
def main():
    # login_url = 'https://eapplication.nitrkl.ac.in/nitris/Login.aspx'
    username = '223cs3144'
    password = '#############'

    driver = None  # Initialize the driver outside the try block
    try:
            # Configure and initialize the Edge webdriver
            driver = configure_webdriver()

            # Perform the login
            perform_login(driver, username, password)
            # Result 
            result(driver)

    finally:
            if driver is not None:
                # Close the webdriver if it is initialized
                driver.quit()

                # Display success message after a successful login
                print("Login successfully!")
        

if __name__ == "__main__":
    main()
