from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import shlex
import subprocess
from info import BASE_DIR, USER_ID, USER_PASS

print(USER_ID)
BASE_DIR = BASE_DIR+"/"
file_name = "geckodriver"
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path = BASE_DIR + file_name)

driver.get("https://github.com/login")

login_box = driver.find_element_by_id("login_field")
print("Logging in using credentials.......")
login_box.send_keys(USER_ID)
passwd_box = driver.find_element_by_id("password")
passwd_box.send_keys(USER_PASS)
passwd_box.send_keys(Keys.RETURN)
time.sleep(1)

print("Initiating new repo creation.......")
driver.get("https://github.com/new")
time.sleep(1)
print("Enter Your Repo Name: ")
repoName = input()
print("Enter Your Repo description: ")
repoNotes = input()
title_box = driver.find_element_by_id("repository_name")
title_box.send_keys(repoName)
desc_box = driver.find_element_by_id("repository_description")
desc_box.send_keys(repoNotes)
time.sleep(2)
button_go = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/form/div[3]/button")
button_go.click()
time.sleep(1)
repo_link_elem = driver.find_element_by_id("empty-setup-clone-url")
repo_link = repo_link_elem.get_attribute("value")
print("Your remote repository link is : " + repo_link)
subprocess.call(shlex.split('bash ./setupGit.sh ' + repo_link ))
