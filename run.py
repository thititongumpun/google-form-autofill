from selenium import webdriver
import random, time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

#option.add_argument("--headless") disable GUI
#option.add_argument("disable-gpu") disable GUI

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=option)

brower.get('Some Google Form url Here...')
time.sleep(2)

q1List = ['//*[@id="i7"]','//*[@id="i10"]']
random_q1 = random.choice(q1List)
q1 = browser.find_element_by_xpath(random_q1).click()
time.sleep(1)

q2List = ['//*[@id="i20"]','//*[@id="i23"]']
random_q2 = random.choice(q2List)
q2 = browser.find_element_by_xpath(random_q2).click()
time.sleep(1)

q3List = ['//*[@id="i39"]','//*[@id="i42"]']
random_q3 = random.choice(q3List)
q3 = browser.find_element_by_xpath(random_q3).click()
time.sleep(1)

q4 = browser.find_element_by_xpath('//*[@id="i52"]').click()
time.sleep(1)

q5List = ['//*[@id="i62"]','//*[@id="i65"]']
random_q5 = random.choice(q5List)
q5 = browser.find_element_by_xpath(random_q5).click()
time.sleep(1)

q6List = ['//*[@id="i84"]','//*[@id="i87"]']
random_q6 = random.choice(q6List)
q6 = browser.find_element_by_xpath(random_q6).click()
time.sleep(1)

nextButton = browser.find_element_by_xpath('//*[@role="button"]').click()
time.sleep(1)

q7List = ['//*[@id="i14"]','//*[@id="i17"]']
random_q7 = random.choice(q7List)
q7 = browser.find_element_by_xpath(random_q7).click()
time.sleep(1)

q8List = ['//*[@id="i30"]','//*[@id="i33"]']
random_q8 = random.choice(q8List)
q8 = browser.find_element_by_xpath(random_q8).click()
time.sleep(1)

q9List = ['//*[@id="i49"]','//*[@id="i52"]']
random_q9 = random.choice(q9List)
q9 = browser.find_element_by_xpath(random_q9).click()
time.sleep(1)

q10List = ['//*[@id="i68"]','//*[@id="i71"]']
random_q10 = random.choice(q10List)
q10 = browser.find_element_by_xpath(random_q10).click()
time.sleep(1)

q11List = ['//*[@id="i87"]','//*[@id="i90"]']
random_q11 = random.choice(q11List)
q11 = browser.find_element_by_xpath(random_q11).click()
time.sleep(1)

q12List = ['//*[@id="i106"]','//*[@id="i109"]']
random_q12 = random.choice(q12List)
q12 = browser.find_element_by_xpath(random_q12).click()
time.sleep(1)

q13List = ['//*[@id="i125"]','//*[@id="i128"]']
random_q13 = random.choice(q13List)
q13 = browser.find_element_by_xpath(random_q13).click()
time.sleep(1)

q14List = ['//*[@id="i144"]','//*[@id="i147"]']
random_q14 = random.choice(q14List)
q14 = browser.find_element_by_xpath(random_q14).click()
time.sleep(1)

q14 = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div[2]').click()
time.sleep(5)

print('DONE')

browser.close()