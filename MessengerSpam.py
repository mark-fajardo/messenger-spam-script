from selenium import webdriver
import time
import sys
import random


# Class MessengerSpam
# @author Mark Joshua Tolentino Fajardo <mjt.fajardo@gmail.com>
# @date Jul 22 2020
class MessengerSpam:
    # MessengerSpam constructor
    # Set spam tries
    def __init__(self, tries):
        self.oBrowser = webdriver.Chrome('D:\DOWNLOADS\chromedriver_83\chromedriver')
        self.iTries = tries

    # Login user with the given params
    def login_user(self, username, pw):
        try:
            self.manage_login(username, pw)

        except Exception as e:
            print('Cannot proceed in logging in.')
            print(e)

    # Login user action
    def manage_login(self, username, pw):
        print('Logging in user...')
        username_in = self.oBrowser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[4]/div/div/form/div/input[7]')
        username_in.send_keys(username)

        pw_in = self.oBrowser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[4]/div/div/form/div/input[8]')
        pw_in.send_keys(pw)

        login_btn = self.oBrowser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[4]/div/div/form/div/button')
        login_btn.click()

    # Method for spamming
    def spam_anyone(self):
        print('Spamming someone...')
        try:
            # You can add as many as you want
            random_string = ['Spam Message 1', 'Spam Message 2', 'Spam Message 3', 'Spam Message 4']

            # Loop spam tries, and spam selected user
            for x in range(int(self.iTries)):
                random.shuffle(random_string)
                print('Spamming attempt ' + str(x + 1))
                msg_in = self.oBrowser.find_element_by_css_selector('.notranslate')
                msg_in.send_keys(random_string[0])

                time.sleep(.3)
                send_btn = self.oBrowser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a')
                send_btn.click()

        except Exception as e:
            print('Spamming stopped.')
            print(e)

    # Initialize browser link
    def init_browser(self, user):
        self.oBrowser.get('https://www.messenger.com/t/' + user)

    # Set specific tries to spam the user
    def set_tries(self, tries):
        self.iTries = tries


# Run class' methods and validate params
# To Run in command line
# python MessengerSpam.py <action> <username> <password> <username_of_target> <tries>
oMessengerSpam = MessengerSpam(10)
aParams = sys.argv

if aParams[1] == 'init':

    # Username to spam must be existing
    if aParams[4] == '':
        print('Username to spam is needed...')

    else:
        # Run user's conversation
        oMessengerSpam.init_browser(aParams[4])
        time.sleep(3)

        # Username and PW is needed.
        if aParams[2] != '' and aParams[3] != '':
            oMessengerSpam.login_user(aParams[2], aParams[3])
            time.sleep(3)

        else:
            print('Username and password is a must...')

        # Number of tries is not required, but you can set it.
        if aParams[5] != '':
            oMessengerSpam.set_tries(aParams[5])
        oMessengerSpam.spam_anyone()
