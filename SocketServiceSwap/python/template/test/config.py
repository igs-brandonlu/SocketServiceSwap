# coding: utf-8

class Hostname(object):
    _002 = "dragon-mjsocket-002-test"
    pass


# gs設定檔文件路徑
ark_server_cfg_folder = "/etc/igs/Mahjong/Game/config/test/"
ark_server_cfg_path = ark_server_cfg_folder + "ark_server.cfg"


# ark_server.cfg
ark_server_cfg = """
[ArkServer]
CodeName = Mahjong
DatabaseName = Ark
RedisHost = dragon-redis-008-test
RedisPort = 6379
MongoHost = 127.0.0.1
MongoPort = 27018
AutoID = 10000000
GMTTime = 8
CurrencyCode =CNY
LogLevel = DEBUG
MongoPoolSize = 30
RedisPoolSize = 30
SocketTimeout = 3
LoggerName = ErrorLog
CollName = ErrorLog

LicenseServer=http://172.32.128.14:8000/check
LicenseApp=dragon
LicenseKey= 1078bbc1ab497532dc79eb5c1bf7fc12

[TableSystem]
RedisHost = dragon-fishredis-001-test
RedisPort = 6379
RedisDB = 1

#Local lan ip mapping

"""
local_lan_ip_mapping = {
    Hostname._002:
        (
            "# {}".format(Hostname._002),
            "L18.140.224.135.5000 = 172.32.72.89:5000",
            "L18.140.224.135.5001 = 172.32.72.89:5001"
        ),
}


# 查看玩家是否都離線的資料庫連線設定
mongo_host = "mongo"
mongo_port = 28023
mongo_db_name = "Match"
mongo_collection_name = "MatchTable"
server_name_to_url_list = {
    Hostname._002: [
        "18.140.224.135:5000", "18.140.224.135:5001"
    ],
}

