import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time


def url_open(url):
    adders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0     Win64     x64     rv:67.0) Gecko/20100101 Firefox/67.0"}
    fw = urllib.request.Request(url, headers=adders)  # 模拟浏览器
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.stylesheet", 2)  # 取消css
    fp.set_preference("permissions.default.image", 2)  # 取消img
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get(url)
    time.sleep(2)
    return driver.page_source


def init(folder):  # 初始化工作目录
    os.mkdir(folder)
    os.chdir(folder)


def savems(folder, melist):  # 保存
    with open(folder, "w")as f:
        for each in melist:
            f.write(each + "\n")
        f.close()


def main(folder="message"):
    init(folder)
    url = "http://www.gaoyuanlight.com/goods?id = 60287&tdsourcetag = s_pctim_aiomsg"
    html = url_open(url)
    soup = BeautifulSoup(html, "lxml")
    messagelist = []
    for each in soup.find_all("div", attrs={"class": "itm"}):
        messagelist.append(each.get_text())
    savems(folder, messagelist)
    print(messagelist)


main()
