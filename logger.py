'''
Description: 日志
Autor: lwk
Date: 2021-04-26 14:19:20
LastEditors: lwk
LastEditTime: 2021-07-17 21:48:17
'''
# -*- encoding:utf-8 -*-
import os
import sys
import datetime
root_path = os.path.abspath(os.path.dirname(__file__))
import logging

def get_logger(name, log_path = None, log_level = 'DEBUG'):
    # create logger
    logger_name = name
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level.upper())

    # create file handler
    if log_path == None:
        curDay = str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)
        log_path = os.path.join(root_path, "log/{}.log".format(curDay))
    if not os.path.exists(log_path):
        file = open(log_path, 'w', encoding='utf8')
        file.close()
    std_h = logging.StreamHandler(sys.stdout)
    std_h.setLevel(log_level.upper())
    fh = logging.FileHandler(log_path, encoding='utf-8')
    fh.setLevel(log_level.upper())

    # create formatter
    fmt = "[%(asctime)-15s] %(levelname)s %(filename)s %(lineno)d %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # add handler and formatter to logger
    fh.setFormatter(formatter)
    std_h.setFormatter(formatter)
    # logger.addHandler(fh)
    logger.addHandler(std_h)
    return logger
logger = get_logger("log", log_level='DEBUG')
if __name__ == "__main__":
    logger = get_logger("MyLog", log_level='DEBUG')
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
