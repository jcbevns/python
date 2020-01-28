from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import os


user = "jcbevns"
passwd = os.environ["FERAL_PASS"]

#Fetch webpage and login via direct link
driver = webdriver.Firefox()
driver.get('https://'+ user + ":" + passwd +"@poseidon.feralhosting.com/jcbevns/rutorrent/.")


try:
    wait(driver, 5).until(EC.presence_of_element_located((By.ID, 'mnu_add')))
    print("Logged in successfully...")
except TimeoutException:
    print("Loading took too much time!")

wait(driver, 3).until(EC.invisibility_of_element_located((By.ID, 'cover')))
add_button = driver.find_element_by_id('mnu_add')
add_button.click()

magnet_url = sys.argv
print('Argument read...')
url_input = driver.find_element_by_id('url')
url_input.send_keys(magnet_url[1])
#url_input.send_keys(Keys.RETURN)

add_url = driver.find_element_by_id('add_url')
add_url.click()
print('Torrent Mangnet added')
driver.close()
