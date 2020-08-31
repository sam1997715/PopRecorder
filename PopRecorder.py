import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
fileNameTime = datetime.datetime.now().strftime("%Y.%m.%d")

xinzhuangURL = "https://www.xzsports.com.tw/parser.php"
getXZ = requests.get(xinzhuangURL)
soupXZ = BeautifulSoup(getXZ.text ,'html.parser')
XZPop = str(soupXZ).split(",")
poolPopXZ = XZPop[1]
gymPopXZ = XZPop[0]


luzhouURL = "https://lzcsc.cyc.org.tw/api"
getLZ = requests.get(luzhouURL)
soupLZ = eval(str(BeautifulSoup(getLZ.text ,'html.parser')))
poolPopLZ = soupLZ["swim"][0]
gymPopLZ = soupLZ["gym"][0]


sanchongURL = "http://www.scsports.com.tw/proxy1.php"
getSC = requests.get(sanchongURL)
soupSC = eval(str(BeautifulSoup(getSC.text ,'html.parser')))
poolPopSC = soupSC["swim"][0]
gymPopSC = soupSC["gym"][0]


taipeiURL = "http://booking.tpsc.sporetrofit.com/Home/loadLocationPeopleNum"
getTP = requests.post(taipeiURL)
soupTP = eval(str(BeautifulSoup(getTP.text ,'html.parser')))
poolPopDA = soupTP['locationPeopleNums'][1]['swPeopleNum']
gymPopDA = soupTP['locationPeopleNums'][1]['gymPeopleNum']
poolPopDT = soupTP['locationPeopleNums'][2]['swPeopleNum']
gymPopDT = soupTP['locationPeopleNums'][2]['gymPeopleNum']


savefile = open(".\\運動人流記錄檔" + fileNameTime + ".txt","a+")
savefile.write(time + "新莊泳池: " + poolPopXZ + "  新莊健身房: " + gymPopXZ + "  蘆洲泳池: " + poolPopLZ + "  蘆洲健身房: " + gymPopLZ + "  三重泳池: " + poolPopSC + "  三重健身房: " + gymPopSC + "  大安泳池: " + poolPopDA + "  大安健身房: " + gymPopDA + "  大同泳池: " + poolPopDT + "  大同健身房: " + gymPopDT + "\n")
savefile.close()
