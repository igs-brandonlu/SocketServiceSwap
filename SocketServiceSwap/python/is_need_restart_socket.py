# coding: utf-8

import sys
from config import restart_socket


def main(hostname):
    return hostname in restart_socket


if __name__ == "__main__":
    if len(sys.argv) > 1:
        result = main(sys.argv[1])
        if result:
            print("yes")
        else:
            print("no")
    else:
        print("no")
