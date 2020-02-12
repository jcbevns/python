from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import os
import argparse

parser = argparse.ArgumentParser()

user = "jcbevns"
passwd = os.environ["PASS_ONE"]


try:
    folderFlag = sys.argv[1]
except IndexError:
    print("You must supply folder destination flag")
    sys.exit(2)


#Fetch webpage and login via direct link
driver = webdriver.Firefox()
driver.get('http://jcbevns.poseidon.feralhosting.com:8080/')

usernameLogin = driver.find_element_by_id('username')
usernameLogin.send_keys(user)

usernameLogin = driver.find_element_by_id('password')
usernameLogin.send_keys(passwd)

usernameLogin = driver.find_element_by_id('login')
usernameLogin.click()
print("Logged in successfully...")


#define flags for paths
folderFlag = str(sys.argv[1])
magnet_url = str(sys.argv[2])
print('Argument read...')

#navigate to download page
driver.get('http://jcbevns.poseidon.feralhosting.com:8080/download.html')

wait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#urls')))
url_input = driver.find_element_by_name('urls')
url_input.send_keys(magnet_url)
#url_input.send_keys(Keys.RETURN)

save_path = driver.find_element_by_name('savepath')

#-f folder
parser.add_argument("folder", help="destination folder")
parser.add_argument("magnet",help="magnet link")

#parse arguments
args = parser.parse_args()

savePath = driver.find_element_by_name('savepath')
moviePath = "/www/jcbevns.poseidon.feralhosting.com/public_html/links/Movies/"
tvPath = "/www/jcbevns.poseidon.feralhosting.com/public_html/links/TV Series/"
musicPath = "/www/jcbevns.poseidon.feralhosting.com/public_html/links/Music/"
tempPath = "/www/jcbevns.poseidon.feralhosting.com/public_html/links/Temporary/"


if args.folder == 'movies':
    savePath.send_keys(moviePath)
elif args.folder == 'tv':
    savePath.send_keys(tvPath)
elif args.folder == 'music':
    savePath.send_keys(musicPath)
elif args.folder == 'temp':
    savePath.send_keys(tempPath)
else:
    print("You didn't specify movies, tv, music, temp")



#add_url = driver.find_element_by_id('submitButton')
#add_url.click()
print('Torrent Mangnet added')
#driver.close()
