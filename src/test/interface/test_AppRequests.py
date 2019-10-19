#-*-coding:utf-8-*-

import unittest
import requests

class test_AppRequests(unittest.TestCase):


    @classmethod
    def setUpClass(self):

        self.host = 'http://172.20.0.195:9093'

    def getCode(self):
        params = {'areaCode': '66',
                  'mobile': '0912345678',
                  'appVersion': '2.4.2',
                  'platform': 'ios',
                  'scene': 'login'
                  }
        response01 = requests.get(self.host+'/user/verifyCode',params=params)
        code = response01.json ()["data"]["code"]
        return code

    @property
    def getUserToken(self):
        data = {'areaCode': '66',
                  'mobile': '0912345678',
                  'appVersion': '2.4.2',
                  'platform': 'Android',
                  'code': self.getCode()
                  }
        response02 = requests.post(self.host+'/user/mobileLogin',data)
        userToken = response02.json()["data"]["userToken"]
        # print(userToken)
        return userToken

    def test_getuserinfo(self):

        self.headers = {'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': 'Android SDK built for x86(Android/9) (com.orderplus.androidapp/1.0) Weex/0.9.4 1080x1794',
                        'countryCode': '66',
                        'languageType': 'TH',
                        'appVersion': '2.4.2',
                        'platform': 'Android',
                        'uuid': '862155035741833',
                        'Authorization': self.getUserToken
                        }
        params = {
                        'countryCode':'66',
                        'languageType':'TH',
                        'appVersion': '2.4.2',
                        'platform':'Android',

        }
        response = requests.get(self.host+'/user/getUserInfo',params=params,headers=self.headers)
        print(response.json())
        # userToken2 = response.json ()["data"]["userToken"]
        # print(userToken2)
        # self.assertEqual(userToken2, self.getUserToken, msg="The same")



