
import os

import allure
import pytest
import requests


from comms.constants import DATA_DIR
from comms.log_utils import logger
from comms.public_api import get_yaml_data


@allure.epic('自动化接口')
@allure.feature('注册接口')
class TestBusinessRegister:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'business_register.yaml'))
    ids = ['测试:{}'.format(case['case_title']) for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_business_register(self, case, db):
        allure.dynamic.title(case['case_title'])

        if case['case_id'] in (1,10):
            db.cud("delete from my_user where  username=%s  ",
                        (case['case_data']['username'], ))

        response = requests.post(url=case['url'], data=case['case_data'])
        res = response.json()
        try:
            assert res == case['expect']
            if case['case_id'] in (1, 10):
                db.find_count('select * from my_user where username=%s', (case['case_data']['username'],))
        except Exception as e:
            logger.error('测试失败,期望结果为:{}', '实际结果为:{}'.format(case['expect'], res))
            logger.exception(e)
            raise e
        else:
            logger.info('测试成功,测试编号为:{},测试场景:{}'.format(case['case_id'], case['case_title']))


if __name__ == '__main__':
    pytest.main(['-vs', './test_register.py'])
