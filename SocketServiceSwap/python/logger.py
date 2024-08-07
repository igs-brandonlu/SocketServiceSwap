# coding: utf-8

import logging
import datetime


def get_logger(logger_name, log_level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setLevel(log_level)
    sh.setFormatter(formatter)
    log_filename = '{}.log'.format(logger_name)
    fh = logging.FileHandler(log_filename)
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger

