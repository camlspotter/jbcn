#!/usr/bin/python3

import time
from selenium import webdriver
from sys import argv
import re
from pathlib import Path

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
user_path= home + '/.jbcn'
#
##############################################################################

# $ jbcn.py [start|end]

f = open(user_path, "r")
lines = f.readlines()
f.close()

if len(lines) != 1:
    print("Error: user_path file must contain only one line")

m = re.match("([^:]+):([^:\n\r]+)[\r\n]+", lines[0])
if not m:
    print("Error: user_path format error")

email=m.group(1)
password=m.group(2)

# print("email=%s password=%s.\n" % (email, password))

mode=str(argv[1])

ids = {
    "start": "adit-button-work-start",
    "end": "adit-button-work-end"
}

id = ids[mode]

driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.

driver.get('https://ssl.jobcan.jp/employee');

time.sleep(5) # Let the user actually see something!

e = driver.find_element_by_id("client_id")
e.send_keys("asahinet")
    
e = driver.find_element_by_id("email")
e.send_keys(email)
    
e = driver.find_element_by_id("password")
e.send_keys(password)

e.submit()    

time.sleep(5) # Let the user actually see something!

e = driver.find_element_by_id(id)
e.click()    
    
time.sleep(5) # Let the user actually see something!

driver.quit()
