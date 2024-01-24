# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:13:51 2024

@author: Gobind
"""

from selenium import webdriver
import sys



driver = webdriver.Edge()
url = "https://www.quora.com/"

driver.get(url)
get_source = driver.page_source

#search function
def search():
    
    while True:
        #Take Word or phrase
        search = input("\nPlease enter the String:\n")
        
        #search whether word or phrase is present or Not?
        
        if search in get_source :
            #if presnt then Print "Object" is present.
            print( f"'{search}' is present in Website")
            
        else:
            #if not present
            print(f"{search} is not presnt")
 
    
#Save page as HTML file
def Savehtml():
    
    url = "https://www.quora.com/"
    driver.get(url)
    
    html_file_path = r"C:\SoftwareTestingLab\Day3\Homework\quora_text_search.html"
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    print(f"Result saved as HTML: {html_file_path}")
   


#end function
def end():
    driver.quit()
    sys.exit(0)


def main():
   
        try:
            #invoke file save method
            Savehtml()
            while True:
                n= int(input("\n\n1.Search\n2.End\nEnter Option: "))
                if n==1:
                    search()
                elif n==2:
                    #invoke Search Function
                    end()
                else:
                    print("------Invalid input------")
        except ValueError:
            print("------Invalid input. Please enter a valid integer------")
        
    
if __name__ == "__main__":
    main()



