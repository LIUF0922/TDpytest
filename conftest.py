import pytest

from comms.database_utils import DBUtils


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的name和nodeid的中文显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        print(i.nodeid)
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='class', autouse=True)
def db():
    print('类开始前运行')
    d = DBUtils()
    yield d
    d.close()
    print('类结束后运行')
