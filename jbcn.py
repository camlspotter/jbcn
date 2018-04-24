#!/usr/bin/python3

import time
from sys import argv
import re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

home = str(Path.home())

########################################################################## You need
#
# * apt install python3-selenium
# * Chrome
#
# * ChromeDriver available at https://sites.google.com/a/chromium.org/chromedriver/
#   The location of the binary:
chromedriver_path= home + '/Downloads/chromedriver/chromedriver'
#
# * The email+password file.  It must have only one line of <email>:<password>.
#   Drop the accessibility form the others.
#   Example: 1009999:mypassword
user_path= home + '/.jbcn'
#
##############################################################################

# $ jbcn.py [start|end]

f = open(user_path, "r")
lines = f.readlines()
f.close()

if len(lines) != 1:
    print("Error: password file must contain only one line")
    exit(1)

m = re.match("([^:]+):([^:\n\r]+)[\r\n]+", lines[0])
if not m:
    print("Error: password format error")
    exit(1)

email=m.group(1)    # It is called "email" in the HTML.
password=m.group(2)

mode=str(argv[1])

ids = {
    "start": "adit-button-work-start",
    "end": "adit-button-work-end"
}

id = ids[mode]

if not id:
    print("jbcn [start|end]")
    exit(1)

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)

driver.get('https://ssl.jobcan.jp/employee');

time.sleep(5) # Let the user actually see something!

# Fill the form, then submit it

e = driver.find_element_by_id("client_id")
e.send_keys("asahinet")
    
e = driver.find_element_by_id("email")
e.send_keys(email)
    
e = driver.find_element_by_id("password")
e.send_keys(password)

e.submit()    

time.sleep(5) # Let the user actually see something!

# click start or end
e = driver.find_element_by_id(id)
e.click()    
    
time.sleep(5) # Let the user actually see something!

driver.quit()
