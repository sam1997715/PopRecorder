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
soupLZ = str(BeautifulSoup(getLZ.text ,'html.parser'))
LZPop = eval(soupLZ)
poolPopLZ = LZPop["swim"][0]
gymPopLZ = LZPop["gym"][0]


sanchongURL = "http://www.scsports.com.tw/proxy1.php"
getSC = requests.get(sanchongURL)
soupSC = str(BeautifulSoup(getSC.text ,'html.parser'))
SCPop = eval(soupSC)
poolPopSC = SCPop["swim"][0]
gymPopSC = SCPop["gym"][0]


taipeiURL = "http://booking.tpsc.sporetrofit.com/Home/LocationPeopleNum"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 啟動無頭模式
chrome_options.add_argument('--disable-gpu') # windowsd必須加入此行
chrome_options.add_argument('log-level=2')
Options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webdriver_path = '.\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = webdriver_path ,options = chrome_options)
driver.get(taipeiURL) #前往這個網址
poolPopDA = driver.find_element_by_xpath("//form[@id = 'form1']/div[@class = 'page']/div[@id = 'main']/div[@class = 'wrapper']/div[@class = 'shell']/div[@class = 'main']/div[@class = 'row']/div[@id = 'EachLidPeopleNumDiv']/div[@class = 'col-md-6']/div[@class = 'tra']/div[@class = 'tra-body']/div[@class = 'tra-space']/p/span[@id = 'CurSwPNum_DASC']").text
gymPopDA = driver.find_element_by_xpath("//form[@id = 'form1']/div[@class = 'page']/div[@id = 'main']/div[@class = 'wrapper']/div[@class = 'shell']/div[@class = 'main']/div[@class = 'row']/div[@id = 'EachLidPeopleNumDiv']/div[@class = 'col-md-6']/div[@class = 'tra']/div[@class = 'tra-body']/div[@class = 'tra-space']/p/span[@id = 'CurGymPNum_DASC']").text
poolPopDT = driver.find_element_by_xpath("//form[@id = 'form1']/div[@class = 'page']/div[@id = 'main']/div[@class = 'wrapper']/div[@class = 'shell']/div[@class = 'main']/div[@class = 'row']/div[@id = 'EachLidPeopleNumDiv']/div[@class = 'col-md-6']/div[@class = 'tra']/div[@class = 'tra-body']/div[@class = 'tra-space']/p/span[@id = 'CurSwPNum_DTSC']").text
gymPopDT = driver.find_element_by_xpath("//form[@id = 'form1']/div[@class = 'page']/div[@id = 'main']/div[@class = 'wrapper']/div[@class = 'shell']/div[@class = 'main']/div[@class = 'row']/div[@id = 'EachLidPeopleNumDiv']/div[@class = 'col-md-6']/div[@class = 'tra']/div[@class = 'tra-body']/div[@class = 'tra-space']/p/span[@id = 'CurGymPNum_DTSC']").text
driver.quit()


savefile = open(".\\運動人流記錄檔" + fileNameTime + ".txt","a+")
savefile.write(time + "新莊泳池: " + poolPopXZ + "  新莊健身房: " + gymPopXZ + "  蘆洲泳池: " + poolPopLZ + "  蘆洲健身房: " + gymPopLZ + "  三重泳池: " + poolPopSC + "  三重健身房: " + gymPopSC + "  大安泳池: " + poolPopDA + "  大安健身房: " + gymPopDA + "  大同泳池: " + poolPopDT + "  大同健身房: " + gymPopDT + "\n")
savefile.close()
