from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
import time
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    

try:
  driver = webdriver.Chrome(chrome_options=options)
  driver.set_window_size(2000, 2000)
  wait = WebDriverWait(driver, 8)
  driver.get("https://link-hub.net/581468/fetch-rewards")
  time.sleep(5)
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  except:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="top"]/div[1]/div[1]/mat-icon'))).click()
  except:
    print ("error")
  driver.save_screenshot('screenie.png')
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-download-redirect-wrapper-component/lv-redirect/div[1]/div[1]/div/div/lv-redirect-first-page/lv-download-page/div/div/div/div[2]/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  time.sleep(3)
  driver.quit()
except:
  print ("error")

try:
  driver = webdriver.Chrome(chrome_options=options)
  driver.set_window_size(2000, 2000)
  wait = WebDriverWait(driver, 8)
  driver.get("https://direct-link.net/581468/how-to-install-any-pc")
  time.sleep(5)
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  except:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="top"]/div[1]/div[1]/mat-icon'))).click()
  except:
    print ("error")
  driver.save_screenshot('screenie.png')
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-download-redirect-wrapper-component/lv-redirect/div[1]/div[1]/div/div/lv-redirect-first-page/lv-download-page/div/div/div/div[2]/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  time.sleep(3)
  driver.quit()
except:
  print ("error")


try:
  driver = webdriver.Chrome(chrome_options=options)
  driver.set_window_size(2000, 2000)
  wait = WebDriverWait(driver, 8)
  driver.get("https://direct-link.net/581468/earn-money-for-free")
  time.sleep(5)
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  except:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="top"]/div[1]/div[1]/mat-icon'))).click()
  except:
    print ("error")
  driver.save_screenshot('screenie.png')
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-redirect/div[1]/div[1]/div/div[1]/lv-redirect-first-page/lv-countdown-block/div/mat-card[2]/div[2]/div/div[3]/div/div/lv-button/a'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/lv-root/div[1]/mat-sidenav-container/mat-sidenav-content/div[2]/lv-download-redirect-wrapper-component/lv-redirect/div[1]/div[1]/div/div/lv-redirect-first-page/lv-download-page/div/div/div/div[2]/div/lv-button/a'))).click()
  driver.save_screenshot('screenie.png')
  time.sleep(3)
  driver.quit()
except:
  print ("error") 

