from pytesseract import image_to_string 
from PIL import Image 
from selenium import webdriver
import pytesseract

def get_captcha_text():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    captcha_text = image_to_string(Image.open('screenshot.png'))
    d=captcha_text.split('\n')
    n=d.index('Enter Captcha')
    g=d[n-1]
    g1=re.sub(r'[^\w\s]','',g)
    g2=g1.strip()
    t=g2[:6]
    return t

def login_to_website(url):
    driver = webdriver.Chrome(executable_path=r"C:\Users\radmin\Desktop\darvin\chromedriver_win32\chromedriver.exe")    
    driver.get(url)    
    driver.set_window_size(2000, 1500)
    #find part of the page you want image of
    element = driver.find_element_by_xpath('/html/body/app-root/my-login-form/mat-card/mat-card-content/div/form')
    location = element.location    
    size = element.size    
    driver.save_screenshot('screenshot.png')
    user_id = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    user_id.clear()
    user_id.send_keys('8056********')
    password = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
    password.clear()
    password.send_keys('2***********7')
    captcha = driver.find_element_by_xpath('//*[@id="mat-input-2"]')
    captcha.clear()
    captcha_text = get_captcha_text()
    captcha.send_keys(captcha_text)
    driver.find_element_by_xpath('/html/body/app-root/my-login-form/mat-card/mat-card-content/div/form/div[3]/button').click()

login_to_website('https://web.umang.gov.in/web_new/login')