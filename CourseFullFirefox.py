import requests
import time
from selenium import webdriver


def check_availibility(browser):
    time.sleep(1)
    current_enrollment = browser.find_element_by_xpath(
        '/html/body/p[2]/table[1]/tbody[1]/tr[2]/td[1]/tt[1]').get_attribute('innerHTML')
    limit = browser.find_element_by_xpath(
        '/html/body/p[2]/table[1]/tbody[1]/tr[2]/td[2]/tt[1]').get_attribute('innerHTML')
    return int(current_enrollment) < int(limit)


def setUp(browser, username, password, sln, quarter, year):
    url = 'https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=' + \
        quarter + '+' + year + '&SLN=' + sln
    browser.get(url)
    user_id_box = browser.find_element_by_id('weblogin_netid')
    user_id_box.send_keys(username)
    user_id_box = browser.find_element_by_id('weblogin_password')
    user_id_box.send_keys(password)
    submit_button = browser.find_element_by_name('_eventId_proceed')
    submit_button.click()


def dropCourses(browser, dropSlns):
    for dropSln in dropSlns:
        to_drop_checkbox = browser.find_element_by_xpath(
            f'//tr[input/@value={dropSln}]/td/input')
        to_drop_checkbox.click()


def register(browser, lectureSln, quizSln, dropSlns):
    url = 'https://sdb.admin.uw.edu/students/uwnetid/register.asp'
    browser.get(url)
    dropCourses(browser, dropSlns)
    sln_table_input = browser.find_element_by_xpath(
        '/html/body/div[2]/form[1]/p[2]/table[1]/tbody[1]/tr[2]/td[1]/input[1]')
    sln_table_input.send_keys(lectureSln)
    if quizSln != 'NA':
        sln_table_input = browser.find_element_by_xpath(
            '/html/body/div[2]/form[1]/p[2]/table[1]/tbody[1]/tr[3]/td[1]/input[1]')
        sln_table_input.send_keys(quizSln)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit_button = browser.find_element_by_xpath(
        '/html/body/div[2]/form[1]/input[7]')
    submit_button.click()


def slnToSearchFor(lectureSln, quizSln):
    return quizSln if quizSln != 'NA' else lectureSln


print('DEICLAIMER: This program can only help you register for the classes that you are allowed to enroll in during the period')
print('Use Ctrl + C to terminate')
print()

username = input('Your UW NetID?\n')
password = input('Your UW NetID password?\n')
quarter = input(
    'Which quarter is this for? choose 1 from (AUT, WIN, SPR, SUM)\n')
year = input('What year is this for? (e.g. 2020)\n')
lectureSln = input('SLN of the lecture you want?\n')
quizSln = input(
    'SLN of the quiz section you want? (enter NA if there is no quiz section)\n')
dropSln = input(
    'SLNs to drop? (enter NA if there is none)\ne.g. 10001 10002\n')
dropSlns = dropSln.split()

browser = webdriver.Firefox()
finalSln = slnToSearchFor(lectureSln, quizSln)
setUp(browser, username, password, finalSln, quarter, year)
while not check_availibility(browser):
    print('There are no empty seats now :(')
    browser.refresh()
register(browser, lectureSln, quizSln, dropSlns)
