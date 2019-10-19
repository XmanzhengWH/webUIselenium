#-*-coding:utf-8-*-

import unittest
import requests

class common_funion:
    headers = {'Content-Type': 'application/json;charset=UTF-8',
                    'User-Agent': 'android'
                    }
    host = 'http://172.20.0.195:9093'
    def getCode(self):
        params = {'areaCode': '66',
                  'mobile': '0912345678',
                  'appVersion': '2.4.2',
                  'platform': 'android',
                  'scene': 'login'
                  }
        response01 = requests.get (self.host + '/user/verifyCode', params=params)
        code = response01.json ()["data"]["code"]
        return code

    def getUserToken(self):
        data = {'areaCode': '66',
                  'mobile': '0912345678',
                  'appVersion': '2.4.2',
                  'platform': 'Android',
                  'code': self.getCode()
                  }
        response02 = requests.post(self.host+'/user/mobileLogin',data,headers=self.headers)
        userToken = response02.json()["data"]["userToken"]
        # print(userToken)
        return userToken

if __name__ == '__main__':
    a= common_funion()
    print(a.getUserToken())

