
import allure
import pytest
import requests


from comms.log_utils import logger
from comms.constants import DATA_DIR
from comms.public_api import get_yaml_data
import os




@allure.epic("自动化接口")
@allure.feature("登录测试")
class TestLogin:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'business_login.yaml'))
    ids = ['测试:{}'.format(case["case_title"]) for case in cases]


    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_login(self, case):
        allure.dynamic.title(case['case_title'])

        response = requests.post(url=case['url'], data=case["case_data"])
        res = response.json()
        try:
            assert res == case['expect']
        except AssertionError as e:
            logger.error('测试失败，期望结果为:{},实际结果为:{}'.format(case['expect'], res))
            logger.exception(e)
            raise e
        else:
            logger.info('测试成功,测试编号为:{},测试场景:{}'.format(case['case_id'], case['case_title']))


if __name__ == '__main__':
    pytest.main(['-vs', './test_login.py'])
