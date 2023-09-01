
import os

"""
动态获取路径
"""
# 获取工程根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# 获取测试数据所在目录
DATA_DIR = os.path.join(BASE_DIR, 'data')


# 日志输出的路径
INFO_LOG = os.path.join(BASE_DIR, 'logs/info.log')
ERROR_LOG = os.path.join(BASE_DIR, 'logs/error.log')

# ini文件路径
INI_DATA = os.path.join(BASE_DIR, 'conf/config.ini')

# 结果报告输出目录
REPORT_JSON = os.path.join(BASE_DIR, 'reports/allure_json')
REPORT_HTML = os.path.join(BASE_DIR, 'reports/allure_html')

# 获取用例目录
CASE_DIR = os.path.join(BASE_DIR, 'test_cases/test_business')
