#-*-coding:utf-8-*-
"""
读取配置。这里配置文件用的yaml
"""
import os
from utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'reports')
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
LOCATOR_FILE = os.path.join(BASE_PATH, 'config', 'Locator.yml')
EXCEL_FILE = os.path.join(BASE_PATH, 'data', 'OpAdmin.xlsx')

class Config:
    def __init__(self,config = CONFIG_FILE,locator = LOCATOR_FILE):
        self.config = YamlReader(config).data
        self.locator = YamlReader(locator).data

    def get_config(self,element,index=0):
        """
            yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
            这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

    def get_locator(self,element,index=0):
        return self.locator[index].get (element)