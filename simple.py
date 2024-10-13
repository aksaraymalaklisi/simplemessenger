from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

class simplemessenger():
    def __init__(self, headless=True):
            # Set up Selenium and Chrome
            seloptions = Options()
            seloptions.add_argument(f"user-data-dir={os.path.dirname(__file__)}{os.path.sep}seldata{os.path.sep}")
            headless and seloptions.add_argument("--headless=new")
            self.driver = webdriver.Chrome(options=seloptions)

    def send(self, content, number):
        try:
            # Set url
            url =f"https://web.whatsapp.com/send?phone=+55{str(number)}&text={content}"
            
            # Set implicit wait
            self.driver.implicitly_wait(60) # After 60 seconds, it will timeout.

            # Open url
            self.driver.get(url)
            
            # Press ENTER to send the message
            # Keys.ENTER # This does not work at all, which is impressive, given that it somehow worked before.

            # Send keypresses (in this case, ENTER) after locating the text bar (this can also be used to add text and other content in here.)
            sendenter = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
            sendenter.send_keys(Keys.ENTER)

            # Manually click send button (unused)
            # sendbutton = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]')
            # sendbutton.click()

            # Wait for 5 seconds and close driver.
            time.sleep(5) 
            self.driver.quit()
            # I wanted to solve anything that needed to wait for load with implicitly_wait(), 
            # but because WhatsApp does not send the message immediately, the driver quits before it sends anything, even though it could find the element and press ENTER.
            # This can probably be fixed by checking if a new message was sent or if the text box is empty, which would cause a implicit wait.

        except Exception as exception:
            print('simple:', exception)
    
    def login(self):
        try:
            url = "https://web.whatsapp.com/"

            self.driver.implicitly_wait(60)

            self.driver.get(url)

            # find_elements will return an empty list. An empty list is false.
            if self.driver.find_elements("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas'):
                qrcode = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
                qrcode.screenshot(f'{os.path.dirname(__file__)}{os.path.sep}qrcode.png') # This can be used to show the QR code while headless.
            else:
                 print('simple: qr code not found')
            
            # This attempts to find the "header" in the conversations bar.
            if self.driver.find_elements("xpath", '/html/body/div[1]/div/div/div[2]/div[3]/header/header/div/div[1]/h1'):
                 print('simple: account is logged in')
                 time.sleep(10)
                 print('simple: waiting for sync')
                 return True
            else:
                 print('simple: login failed')
                 return False

        except Exception as exception:
             print('simple:', exception)
             