# -*- coding: utf-8 -*-

import requests
import src.setting as SETTING


class Connect(object):
    '''
    初始化连接
    kd:为职位
    city:为城市
    '''

    def __init__(self, city, kd, first=None, pn=None, gx=None, xl=None, isSchoolJob=None, needAddtionalResult=None):

        if not gx:
            if not first:
                self.para = {'first': 'true', 'pn': '1', 'kd': self.kd, 'city': self.city}
            else:
                self.para['first'] = 'false'
                self.para['pn'] = pn
        else:
            self.city = city
            self.kd = kd
            if not first:
                self.para = {'first': 'true', 'pn': '1', 'kd': self.kd, 'city': self.city, 'gx':gx,
                             'isSchoolJob': isSchoolJob, 'needAddtionalResult':needAddtionalResult}
            else:
                self.para['first'] = 'false'
                self.para['pn'] = pn

    def getConnect(self, timeOut=5):

        headers = SETTING.headers
        cookies = SETTING.cookies


        url = 'https://www.lagou.com/jobs/positionAjax.json'


        response = requests.post(url, data=self.para, headers=headers, cookies=cookies, timeout=timeOut)
        if response.status_code == 200 or response.status_code == 302:
            return response
        else:
            print("GET URL ERROR-----status_code=" + response.status_code)

