import requests
from bs4 import BeautifulSoup
import socks
import socket
import time
import os
from fake_useragent import UserAgent


class my_ip_is:
    def check_ip(self):
        os.startfile(link_on_your_tor)  # here i have tor browser
        time.sleep(8)
        socks.setdefaultproxy(socks.SOCKS5, "localhost", open_port)
        UserAgent().chrome
        socket.socket = socks.socksocket
        dic_user_agent_new = {'User-Agent': UserAgent().chrome}
        responce = requests.get(link_on_website,dic_user_agent_new).text
        bs = BeautifulSoup(responce, 'html.parser')
        block = bs.find("div", id="main")
        find_block_ip = block.find_all('strong')[0].text
        find_block_user_agent = block.find_all('span')[66].text
        print(f"Your ip is: {find_block_ip} ")
        print(f"Your user-agent: {find_block_user_agent} ")
        os.system('TASKKILL /F /IM firefox.exe ') #kill our process
if __name__ =='__main__':
    link_on_website = "https://whoer.net/ru" #website for check
    link_on_your_tor = 'C:/Users/Виктор/Documents/Tor Browser/Browser/firefox.exe'
    open_port = 9150
    x = my_ip_is
    x.check_ip(None)
