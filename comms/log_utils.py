import logging
from comms.constants import INFO_LOG, ERROR_LOG


def get_logger():
    logger = logging.getLogger()
    logger.setLevel('DEBUG')

    sh1 = logging.FileHandler(filename=INFO_LOG, mode='a', encoding='utf-8')
    sh1.setLevel('INFO')

    sh2 = logging.FileHandler(filename=ERROR_LOG, mode='a', encoding='utf-8')
    sh2.setLevel('ERROR')

    logger.addHandler(sh1)
    logger.addHandler(sh2)

    my_fmt = logging.Formatter("%(asctime)s -[%(filename)s - %(lineno)d] -%(levelname)s:%(message)s")
    sh1.setFormatter(my_fmt)
    sh2.setFormatter(my_fmt)
    return logger


logger = get_logger()
