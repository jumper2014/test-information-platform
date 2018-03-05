# coding=utf-8
# author: zengyuetian

import cookielib
import sys
import urllib
import urllib2

from bs4 import BeautifulSoup

from app.main.const import *


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

login_url = 'http://192.168.0.1:8080/zentao/user-login.html'
referer_url = "http://192.168.0.1:8080/zentao/bug-report-1-unclosed-0.html"


class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self, chart_param):
        """

        :param chart_param:
        :return:
        """
        loginparams = {"account": "admin", "password": "adminPass", "keepLogin[]": "on"}
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Accept': "text/html",
            # "Accept-Encoding": "gzip, deflate"

        }
        req = urllib2.Request(login_url, urllib.urlencode(loginparams), headers=headers)
        # req = urllib2.Request(login_url, login_params, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        # print thePage

        query_params = chart_param
        req = urllib2.Request(referer_url, query_params, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        opened_bugs_page = response.read()
        # print opened_bugs_page
        return opened_bugs_page


def parse_newly_bug_html(page):
    date_list = []
    value_list = []
    bugs_dict = {}
    soup = BeautifulSoup(page, "html.parser")
    date_data = soup.find_all(name="td", attrs={'class': 'chart-label'})
    for item in date_data:
        if len(item.contents) == 1:
            # print "contents:", item.contents[0]
            date = str(item.contents[0])
            date_list.append(date)

    value_data = soup.find_all(name="td", attrs={'class': 'chart-value'})
    for item in value_data:
        if len(item.contents) == 1:
            # print "contents:", item.contents[0]
            value_list.append(int(item.contents[0]))

    slice_size = 0 - RECENT_DATE_SIZE
    date_list = date_list[slice_size:]
    value_list = value_list[slice_size:]
    # print date_list
    # print len(date_list)
    bugs_dict = dict(zip(date_list, value_list))
    # print "page:bugs_dict", bugs_dict
    return bugs_dict


def parse_bug_status_html(page):
    category_list = []
    value_list = []
    bugs_status_dict = {}
    soup = BeautifulSoup(page, "html.parser")
    date_data = soup.find_all(name="td", attrs={'class': 'chart-label'})
    for item in date_data:
        if len(item.contents) == 1:
            # print "contents:", item.contents[0]
            category = str(item.contents[0])
            category_list.append(category)

    value_data = soup.find_all(name="td", attrs={'class': 'chart-value'})
    for item in value_data:
        if len(item.contents) == 1:
            # print "contents:", item.contents[0]
            value_list.append(int(item.contents[0]))

    # print date_list
    # print len(date_list)
    bugs_status_dict = dict(zip(category_list, value_list))
    # print "page:bugs_dict", bugs_dict
    return bugs_status_dict


def get_newly_bug_info():
    userlogin = Login()
    param = "charts%5B%5D=openedBugsPerDay"
    ori_page = userlogin.login(param)
    return parse_newly_bug_html(ori_page)


def get_all_bugs_status():
    userlogin = Login()
    param = "charts%5B%5D=bugsPerStatus"
    ori_page = userlogin.login(param)
    # print ori_page
    return parse_bug_status_html(ori_page)

if __name__ == '__main__':
    print get_newly_bug_info()
    print get_all_bugs_status()


