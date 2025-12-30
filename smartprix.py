# PART-1:
# Task is to automate Chrome browser, Where it loads the 'mobile' page of Smartprix website.
# Once it loads We have click LOAD MORE option, so that we reach end of webpage.
# After We can Download html file and do further analysis

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# (1) Since we are  automating browser(in general chrome browser) so we install below.
# - installing chromedriver
# - based on your version of chrome, download chrome driver one version before.
# - ex: my current version is Version 143.0.7499.170 & I have download This (https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.169/win64/chromedriver-win64.zip)
# - open the zip file and get the exe file
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (2) Importing Required Modules
from selenium import webdriver # webdriver is a subpackage
from selenium.webdriver.chrome.service import Service # Service is a class
from selenium.webdriver.common.by import By # By is a Class
from selenium.webdriver.common.keys import Keys # Keys is a Class
import time # time module is needed to add delay while we're requesting webpage
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (3) create service object by passing path of your driver exe file
s = Service("C:/Path/To/chromedriver-win64/chromedriver.exe")

# (4) # To open a Chrome browser write below code and pass driver as a service
driver = webdriver.Chrome(service=s)

# Now Chrome browser is opened programmatically with no web page.
# But Why the browser opens only for 1 second ❓
# Your Python script finishes execution immediately.
# When the script ends:
# The driver object is destroyed & Chrome automatically closes
# So Chrome is not crashing — Python is just exiting.
# SOLUTION: ADD _exit = input("Press Enter To Close the Browser!!!") THIS AT THE END OF CODE

# (5) To open webpage in that Chrome browser pass the url
driver.get("https://www.smartprix.com/mobile")
time.sleep(2) # add delay because we have to respect the server.


# (6) FILTERING WEB PAGE: WE DON'T WANT 'smartphones' WHICH IS 'out of stock' or 'upcoming smartphones'.
# finding exclude_out_of_stock input check box element and clicking
input_element_1 = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
input_element_1.click() # once find click that element
time.sleep(2) # add delay

# Similarly finding exclude_upcoming input check box element and clicking
input_element_2 = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
input_element_2.click()
time.sleep(1)


# (7) LOADING ENTIRE WEBPAGE PROGRAMMATICALLY
# By Default web page gives 20 smartphones, but to get web page we have to  load entire products
# finding load more button and clicking.

# by default height of webpage is
old_height = driver.execute_script('return document.body.scrollHeight')

# So we are loading the web page until and unless we get the full height of the webpage
while True:
    print(f'OLD_HEIGHT: {old_height}') # height before loading web page

    # loading web page
    load_more_button = driver.find_element(by=By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]')
    load_more_button.click()
    time.sleep(1)

    # after loading height of webpage is
    new_height = driver.execute_script('return document.body.scrollHeight')

    print(f'OLD_HEIGHT: {new_height}') # height after loading web page
    print('----------------')
    if new_height == old_height:
        break

    old_height = new_height

# (8) Once the entire webpage is loaded get the html data
html_data = driver.page_source

# As we have html data, now write the html data into html file
with open("smartprix.html",'w',encoding ='utf-8') as fp:
    fp.write(html_data)


_exit = input("Press Enter To Close the Browser!!!")

# (AS OF NOW WE HAVE FULL PRODUCTS ON WEB PAGE, NOW WE CAN USE BeautifulSoup To parse and get the data)

# For that Pls refer "smartprix_to_dataframe.ipynb" file
