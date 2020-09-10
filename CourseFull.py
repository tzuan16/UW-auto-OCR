import requests
import time
from selenium import webdriver

def check_availibility(browser):
    time.sleep(1)
    current_enrollment = browser.find_element_by_xpath('/html/body/p[2]/table[1]/tbody[1]/tr[2]/td[1]/tt[1]').get_attribute('innerHTML')
    limit = browser.find_element_by_xpath('/html/body/p[2]/table[1]/tbody[1]/tr[2]/td[2]/tt[1]').get_attribute('innerHTML')
    return int(current_enrollment) < int(limit)

def setUp(browser, username, password, sln, quarter, year):
    url = 'https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=' + quarter + '+' +  year + '&SLN='+ sln
    browser.get(url)
    user_id_box = browser.find_element_by_id('weblogin_netid')
    user_id_box.send_keys(username)
    user_id_box = browser.find_element_by_id('weblogin_password')
    user_id_box.send_keys(password)
    submit_button = browser.find_element_by_name('_eventId_proceed')
    submit_button.click()

def register(browser, sln, quiz):
    url = 'https://sdb.admin.uw.edu/students/uwnetid/register.asp'
    browser.get(url)
    sln_table_input = browser.find_element_by_xpath('/html/body/div[2]/form[1]/p[2]/table[1]/tbody[1]/tr[2]/td[1]/input[1]')
    sln_table_input.send_keys(sln)
    if quiz != 'NA':
        sln_table_input = browser.find_element_by_xpath('/html/body/div[2]/form[1]/p[2]/table[1]/tbody[1]/tr[3]/td[1]/input[1]')
        sln_table_input.send_keys(quiz)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit_button = browser.find_element_by_xpath('/html/body/div[2]/form[1]/input[7]')
    submit_button.click()

def slnToSearchFor(sln, quiz):
    if quiz != 'NA':
        return quiz
    return sln

print('DEICLAIMER: This program can only help you register for the classes that you are allowed to enroll in during the period')
print('Use Ctrl + C to terminate')
print()
print('Your UW NetID?')
username = input()
print('Your UW NetID password?')
password = input()
print('SLN of the course you want? (not the quiz section)')
sln = input()
print('SLN of the quiz section you want? (enter NA of there is no quiz section)')
quiz = input()
print('Which quarter is this for? choose 1 from (AUT, WIN, SPR, SUM)')
quarter = input()
print('What year is this for? (e.g. 2020)')
year = input()
browser = webdriver.Firefox()
finalSln = slnToSearchFor(sln, quiz)
setUp(browser, username, password, finalSln, quarter, year)
while not check_availibility(browser):
    print('There are no empty seats now :(')
    browser.refresh()
register(browser, sln, quiz)
