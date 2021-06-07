from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import string

import time

#driver = webdriver.Firefox()//403
driver = webdriver.Chrome()

def func_reg(email):
    driver.get('https://hosting.timeweb.ru/login')
    tags = driver.find_elements_by_tag_name('a')  
    for tag in tags:
        print(tag.text)
        if 'Регистрация' in tag.text:            
            tag.click()
            break            

    full_name= name_gen()
    print(driver.window_handles)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(4)
    fields  = driver.find_elements_by_name('full_name')
    
    for field in fields:
        try:
            field.send_keys(full_name)
        except:
            pass
           
    time.sleep(5)
    driver.find_element_by_name('email').send_keys(email)  
    
    print(full_name)
    print(email)
    
    butts = driver.find_elements_by_class_name('hosting-items__button')
    for butt in butts:        
        if butt.text == 'СТАТЬ КЛИЕНТОМ':
            butt.click()
            break
    time.sleep(15)
    
def name_gen():   
    return  ''.join(random.choice(string.ascii_lowercase) for i in range(10))         
 
def get_temp_email():
    driver.get('https://cryptogmail.com/')
    print(driver.window_handles)
    email = driver.find_element_by_class_name('field--value').text
    
    return email    
    
def get_fields():
    
    tags = driver.find_elements_by_class_name('cpS-tooltip-inline')
    for tag in tags:
        print (tag.text)
    field_1 = '???'#tags[0].text
    field_2 = '???'#tags[1].text
    print(field_1, field_2)
    
    tags = driver.find_elements_by_class_name('cpS-h-XS')
    field_3 = tags[4].text
    field_4 = tags[5].text
    
    driver.get('http://127.0.0.1:5000/addForm')      
    driver.find_element_by_name('field_1').send_keys(field_1)
    driver.find_element_by_name('field_2').send_keys(field_2)
    driver.find_element_by_name('field_3').send_keys(field_3)
    driver.find_element_by_name('field_4').send_keys(field_4)
    
    
    driver.find_element_by_id('send').click()
    
func_reg(get_temp_email())
get_fields()
#driver.close()