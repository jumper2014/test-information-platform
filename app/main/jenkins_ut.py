# coding=utf-8
# author: zengyuetian
# get ut information from jenkins builds

import sys
import re
import urllib2
import urllib
import requests
import cookielib
from bs4 import BeautifulSoup


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

login_url = 'http://10.4.0.1:8080/j_acegi_security_check'
builds = ["p2pclient_ut", "p2pserver_ut"]
client_referer_url = "http://10.4.0.1:8080/view/p2pclient_ut/job/p2pclient_ut/lastCompletedBuild/testReport"
server_referer_url = "http://10.4.0.1:8080/view/p2pserver/job/p2pserver_ut/lastCompletedBuild/testReport"


class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self, referer_url=None):
        '''登录网站'''

        login_params = {"j_username": "zengyuetian", "j_password": "vliQh3U2byob", "remember_me": False, "from": "/"}
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Accept': "text/html",
            # "Accept-Encoding": "gzip, deflate"

        }
        # req = urllib2.Request(loginurl, urllib.urlencode(loginparams), headers=headers)
        req = urllib2.Request(login_url, urllib.urlencode(login_params), headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        # thePage = response.read()
        # print thePage

        # req = urllib2.Request(referer_url, None, headers=headers)
        # print referer_url
        # response = urllib2.urlopen(req)
        # print response
        # self.operate = self.opener.open(req)
        # thePage = response.read()
        # return thePage

    def get_ut_data(self, referer_url):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Accept': "text/html",
            # "Accept-Encoding": "gzip, deflate"

        }
        req = urllib2.Request(referer_url, None, headers=headers)
        print referer_url
        response = urllib2.urlopen(req)
        print response
        self.operate = self.opener.open(req)
        thePage = response.read()
        return thePage


def parse_ut_test_html(page):
    ut_test_cases = 0
    soup = BeautifulSoup(page, "html.parser")
    date_data = soup.find_all(name="div", attrs={'align': 'right'})
    for item in date_data:
        if len(item.contents) == 1:
            # print "contents:", item.contents[0]
            number_res = str(item.contents[0])
            # print "number_res:",number_res
            if "tests\n" in number_res and "(±" in number_res:
                ut_test_cases = process_div_get_ut_test(number_res)
                break

    return ut_test_cases


def process_div_get_ut_test(div_string):
    """

    :param div_string:
    :return:
    """
    ut_test_res = 0
    string_token_list = div_string.split("\n")
    for token in string_token_list:
        if "tests" in token:
            tmp_list = token.split(" ")
            if tmp_list[-1] == 'tests':
                ut_test_res = tmp_list[-2]

    return ut_test_res


def get_ut_num():
    """

    :return:
    """
    ut_test_data = {"p2pclient_ut": 0, "p2pserver_ut": 0}
    userlogin = Login()
    userlogin.login()
    ut_test_data['p2pclient_ut'] = int(parse_ut_test_html(userlogin.get_ut_data(client_referer_url)))
    ut_test_data['p2pserver_ut'] = int(parse_ut_test_html(userlogin.get_ut_data(server_referer_url)))
    # ut_test_data['p2pclient_ut'] = int(parse_ut_test_html(userlogin.login(client_referer_url)))
    # ut_test_data['p2pserver_ut'] = int(parse_ut_test_html(userlogin.login(server_referer_url)))

    return ut_test_data

if __name__ == '__main__':
    print get_ut_num()