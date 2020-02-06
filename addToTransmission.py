from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import os

user = ""
passwd = "sI0qQsbk2cl6nCM1"
#passwd = os.environ["FERAL_TRANS"]

#Fetch webpage and login via direct link
driver = webdriver.Firefox()
driver.get('https://:' + passwd + 'poseidon.feralhosting.com/jcbevns/transmission/web/')
#driver.get('https://' + user + ':' + passwd + '@oseidon.feralhosting.com/jcbevns/transmission/web/')


wait(driver, 3).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#toolbar-open')))
add_button = driver.find_element_by_css_selector('#toolbar-open')
add_button.click()

magnet_url = sys.argv
print('Argument read...')

wait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#torrent_upload_url')))
url_input = driver.find_elements_by_id('#torrent_upload_url')
url_input.sele()
url_input.send_keys(magnet_url[1])
#url_input.send_keys(Keys.RETURN)

add_url = driver.find_elements_by_css_selector('#upload_confirm_button')
add_url.click()
print('Torrent Mangnet added')
driver.close()
