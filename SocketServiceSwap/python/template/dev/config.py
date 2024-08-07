# coding: utf-8

# instance name 列表
class Hostname(object):
    _001 = "ark"
    pass


# gs設定檔文件路徑
ark_server_cfg_folder = "/etc/igs/Mahjong/Game/config/dev/"
ark_server_cfg_path = ark_server_cfg_folder + "ark_server.cfg"


# ark_server.cfg
ark_server_cfg = """
[ArkServer]
CodeName = Mahjong
DatabaseName = Mahjong
RedisHost = 127.0.0.1
RedisPort = 6379
MongoHost = 127.0.0.1
MongoPort = 27017
AutoID = 10000000
GMTTime = 8
CurrencyCode =CNY
LogLevel = DEBUG
MongoPoolSize = 30
RedisPoolSize = 30
SocketTimeout = 3
LoggerName = ErrorLog
CollName = ErrorLog

LicenseServer=http://10.4.8.117:8000/check
LicenseApp=samplobby
LicenseKey=346731a77208ad081eb60698d5048b2d

[TableSystem]
RedisDB = 1

[Report]
DatabaseName = JapanMahjongReport
MongoHost = 127.0.0.1
MongoPort = 27017
MongoPoolSize = 30

#Local lan ip mapping

"""
local_lan_ip_mapping = {
    Hostname._001:
        (
            "# {}".format(Hostname._001),
            "L192.168.132.177.5000 = 127.0.0.1:5000"
        ),
}

# 查看玩家是否都離線的資料庫連線設定
mongo_host = "mongo"
mongo_port = 27017
mongo_db_name = "Match"
mongo_collection_name = "MatchTable"
server_name_to_url_list = {
    Hostname._001: [
        "192.168.132.177:5000", "192.168.132.177:5001"
    ],
}
