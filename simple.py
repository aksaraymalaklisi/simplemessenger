import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

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
            
            # Open url and wait 15 seconds
            self.driver.get(url)
            time.sleep(15)
            
            # Press ENTER to send the message
            # Keys.ENTER # This does not work at all, which is impressive, given that it somehow worked before.

            # Send keypresses (in this case, ENTER) after locating the text bar (this can also be used to add text and other content in here.)
            sendmanual = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
            sendmanual.send_keys(Keys.ENTER)

            # Manually click send button (unused)
            # sendbutton = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]')
            # sendbutton.click()

            # Wait for 5 seconds and close driver.
            time.sleep(5)
            self.driver.quit()

        except Exception as exception:
            print(exception)