from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement

window = webdriver.Chrome("C:\chromedriver.exe")

window.get("https://plg.bet/")
loginBtn = window.find_element_by_xpath("/html/body/header/div[2]/a")
steamClick = window.find_element_by_xpath("/html/body/div[11]/div[2]/form/a")


time.sleep(1.5)

class User:
    def __init__(self,user,password,betAmount,betCount):
        self.user = user
        self.password = password
        self.betAmount = betAmount
        self.betCount  = betCount
    def steamLog(self):
        user = window.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div/div[2]/div[2]/div/form[1]/input[4]")
        password = window.find_element_by_xpath(
            "/html/body/div[1]/div[7]/div[2]/div/div[2]/div[2]/div/form[1]/input[5]")
        steamLogin = window.find_element_by_xpath(
            "/html/body/div[1]/div[7]/div[2]/div/div[2]/div[2]/div/form[1]/div[4]/input")
        user.send_keys(self.user)
        password.send_keys(self.password)
        steamLogin.click()
        time.sleep(20)

    def insertBet(self,bet):
        betAmount = window.find_element_by_xpath(
            "/html/body/div[34]/div[2]/div/div[1]/div[4]/div[2]/input")
        betAmount.send_keys(bet)

    def placeBetClick(self):
        placeBet = window.find_element_by_xpath(
            "/html/body/div[34]/div[2]/div/div[2]/div[1]/div[1]/div/button")
        placeBet.click()
    def confirmBetClick(self):
        confirmBet = window.find_element_by_xpath("/html/body/div[1]/div[6]/div/div/div[2]/div[2]/button[1]")
        confirmBet.click()

    def ifUserWin(self):
        lastWin = window.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div[3]/ul/li[10]/span")
        if(lastWin.get_attribute("class") == "red"):
            self.betCount = 1
            User.clearBetField(self)
            User.betting(self)

    def allowBetIfLastFreeSpinsAreLost(self):
        firstLost = window.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div[3]/ul/li[10]/span")
        secondlost = window.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div[3]/ul/li[9]/span")
        thirdLost = window.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div[3]/ul/li[8]/span")
        return (firstLost.get_attribute("class") != "dark" and secondlost.get_attribute("class") != "dark" and thirdLost.get_attribute("class") != "dark"  )
    def doubleBet(self):
        doubleButton = window.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div[4]/div[2]/ul/li[6]/button")
        doubleButton.click()
    def firstBetCondition(self):
        placeBet = window.find_element_by_xpath(
            "/html/body/div[34]/div[2]/div/div[2]/div[1]/div[1]/div/button")
        return ((placeBet.is_enabled() and (self.betCount == 1)))
    def secondBetCondition(self):
        placeBet = window.find_element_by_xpath(
            "/html/body/div[34]/div[2]/div/div[2]/div[1]/div[1]/div/button")
        return ((placeBet.is_enabled() and (self.betCount > 1)))

    def clearBetField(self):
        betAmount = window.find_element_by_xpath(
            "/html/body/div[34]/div[2]/div/div[1]/div[4]/div[2]/input")
        betAmount.clear()

    def betting(self):
        while True:
            print(User.firstBetCondition(self))


            if (User.firstBetCondition(self)):

                User.insertBet(self,"1")
                User.placeBetClick(self)


                print("first bet coditional")
                print(self.betCount)
                self.betCount = self.betCount + 1
                print(self.betCount)
                time.sleep(25)

            elif (robur.secondBetCondition()):
                time.sleep(1)
                User.ifUserWin(self)
                User.doubleBet(self)
                User.placeBetClick(self)
                time.sleep(25)


robur = User("roobson4","","1",1)

loginBtn.click()
time.sleep(1)
steamClick.click()
time.sleep(1.5)
robur.steamLog()

robur.betting()






