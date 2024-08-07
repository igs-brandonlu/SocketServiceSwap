# coding: utf-8

import pymongo
from logger import get_logger
from config import mongo_host, mongo_port, mongo_db_name, mongo_collection_name, get_server_url_list, restart_socket


def main(logger):
    try:
        # 檢查是否有要重啟的機器，沒有即返回-1
        if len(restart_socket) <= 0:
            return -1

        # 連接資料庫
        mongo_client = pymongo.MongoClient(mongo_host, mongo_port)
        db = mongo_client[mongo_db_name]
        collection = db[mongo_collection_name]
        query = {
            "Url": {"$in": get_server_url_list(restart_socket)}
        }
        # 查詢玩家有幾人在線
        count = collection.find(query).count()
        logger.debug("query:{} count: {}".format(query, count))
        return count
    except Exception as e:
        logger.error(e)
        return 9999


if __name__ == "__main__":
    logger = get_logger('check_player_online_count')
    result = main(logger)
    print(result)
