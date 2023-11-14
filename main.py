from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyfiglet import Figlet
from selenium.webdriver.chrome.options import Options
import time

#Welcome Prompt [problem when changing to exe]
# def ascii_art(text, font, width=200):
#     fig = Figlet(font=font, width=width)
#     ascii_art = fig.renderText(text)
#     print(ascii_art)

# ascii_art('Made by K.', font="standard")

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://achieve.hashtag-learning.co.uk/accounts/login/')

while True:
    username_element = browser.find_element_by_xpath('//*[@id="id_login"]')
    password_element = browser.find_element_by_xpath('//*[@id="id_password"]')
    
    username_input = input('E-mail: (only the numbers): ')+'@ea.edin.sch.uk'
    password_input = input('Password: ')
    
    username_element.clear()
    username_element.send_keys(username_input)

    password_element.clear()
    password_element.send_keys(password_input)
    
    sign_in_button = browser.find_element_by_xpath('/html/body/main/div/div[2]/div[2]/div/div/div[2]/form/button').click()
    
    current_url = browser.current_url
    if current_url != 'https://achieve.hashtag-learning.co.uk/accounts/login/':
        break
    else:
        print('Login information given incorrectly, please try again.')
        continue

#main page [CHANGE IF NEEDED]
course = browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[1]/div/div[2]/div[1]/div[1]/form/button').click()
#click on nav bar

#getting streak
def get_streak():
    asses_button = browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[4]/a').click()
    def_streak_parent = browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[3]/div/div[2]/div[2]/div[1]')
    streak_text = def_streak_parent.text
    return int(streak_text.split(':')[-1].strip())

def_streak = get_streak()
print(f'\nBest Streak: {def_streak}')
while True:
    required_streak = int(input('What streak would you like to reach?\n'))
    estimated_time_seconds = round((0.9446296691894531 + 0.22640132904052734) * (required_streak - def_streak) + 0.2739546298980713, 2)
    hours, remainder = divmod(estimated_time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if required_streak > def_streak:
        if required_streak - def_streak > 2000:
            consent_huge_streak = input(f'Estimated total time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds, do you give consent? (y/n)')
            if consent_huge_streak == "y" or consent_huge_streak == "Y":
                break
            else:
                print('\nConsent not given, try again.')
                continue
        break
    else:
        print('\nThe required streak must be greater than the current best streak, try again.')

print(f'Estimated total time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds')

def question_loop():
        #click on asses_topic
        asses_topic = browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div/div[2]/div[1]/div[2]/a').click()

        #click on environmental_impact [CHANGE IF NEEDED]
        target_topic = browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[3]/div/div[2]/div[8]/div/a').click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[2]/main/div/form/div/div/div[2]/div/div[1]/div/button'))).click() #wait for button to be clickable
        #question page
        question_parent = browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div[1]/div/div')#getting question
        question = question_parent.text
        
        #checking which question it is [CHANGE FOR DIFFERENT TOPICS (ADD OR REMOVE)]
        questions = {
                'Which of the following is NOT an environmental benefit to using an intelligent heating system?': 1,
                'Which of the following is an environmental benefit to using an intelligent car management system?': 2,
                'Which of the following is an environmental benefit to using an intelligent traffic control system?': 3,
            }
        #setting variables for correct choices [NEED TO ASSIGN CORRECT CHOICES FOR EACH QUESTION, 1 BY 1]
        correct_choices = {
            1: 'Switch heating on / off using a timer',
            2: 'Start-stop systems shut down the engine when they detect that the car is stationary',
            3: 'Software, sensors and cameras can be used to reduce traffic flow',
        }
        question_no = questions.get(question, 0)
        correct = correct_choices.get(question_no)

        #getting choices
        choices = []
        parent_choices = [browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div[1]'), browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div[1]'), browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div[1]'), browser.find_element_by_xpath('/html/body/main/div/div[2]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]')]
        for i in range(len(parent_choices)):
            choices.append(parent_choices[i].text)
        #getting buttons
        button = []
        for i in range(4):
            button.append(browser.find_element_by_xpath(f'//*[@id="button_{i+1}"]'))
        #clicks the right choice
        for choice in choices:
            if choice in correct:
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="button_{choices.index(choice) + 1}"]'))).click()
        browser.back()

start_time = time.time()
while True:  
    def_streak = get_streak()
    
    print(f'Current Streak: {def_streak}') 
    if def_streak == required_streak:
        break
    question_loop() 
# ascii_art('Streak reached successfully!', font="small")
end_time = time.time()
actual_time_seconds = round(end_time - start_time, 2)
hours, remainder = divmod(actual_time_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f'Total time taken: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds')