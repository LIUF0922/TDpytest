from configparser import ConfigParser
import requests
import yaml
from comms.constants import INI_DATA


def get_yaml_data(file):
    try:
        with open(file, mode='r', encoding='utf-8') as fr:
            cases = yaml.safe_load(fr)
        return cases
    except Exception as e:
        print('从yaml文件读取测试数据失败！', e)


def get_ini_data(section, option):
    try:
        cp = ConfigParser()
        cp.read(INI_DATA, encoding='utf-8')
        return cp.get(section, option)
    except Exception as e:
        print("从ini文件中读取数据失败", e)


def get_token():
    try:
        ini_name = get_ini_data('user', 'name')
        ini_pwd = get_ini_data('user', 'password')
        response = requests.post(url='http://127.0.0.1:5000/business/token_login',
                                 data={'username': ini_name, 'password': ini_pwd, 'typeId': 101})
        result = response.json()
        tk = result['token']
        return tk
    except Exception as e:
        print('token获取失败', e)
