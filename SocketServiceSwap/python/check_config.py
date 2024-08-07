# coding: utf-8

import sys
from config import move_out, move_in, restart_socket
from logger import get_logger


def check_move_out(logger):
    #logger.debug("check_move_out : {}".format(move_out))
    return "{}".format(move_out)


def check_move_in(logger):
    #logger.debug("check_move_in : {}".format(move_in))
    return "{}".format(move_in)


def check_restart_socket(logger):
    #logger.debug("check_restart_socket : {}".format(restart_socket))
    return "{}".format(restart_socket)


if __name__ == "__main__":
    logger = get_logger('check_config')
    if len(sys.argv) > 1:
        opt = sys.argv[1]
        if opt.lower() == 'move_out':
            result = check_move_out(logger)
        elif opt.lower() == 'move_in':
            result = check_move_in(logger)
        elif opt.lower() == 'restart_socket':
            result = check_restart_socket(logger)
        else:
            result = "Unknown argv: {}".format(opt)
        print(result)
    else:
        print("Need argv: move_out, move_in, restart_socket")
