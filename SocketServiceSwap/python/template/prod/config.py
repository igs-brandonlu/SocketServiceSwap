# coding: utf-8

# instance name 列表
class Hostname(object):
    _001 = "dragon-mjsocket-001-prod"
    _002 = "dragon-mjsocket-002-prod"
    _003 = "dragon-mjsocket-003-prod"
    _004 = "dragon-mjsocket-004-prod"
    _005 = "dragon-mjsocket-005-prod"
    _006 = "dragon-mjsocket-006-prod"
    pass


# gs設定檔文件路徑
ark_server_cfg_folder = "/etc/igs/Mahjong/Game/config/release/"
ark_server_cfg_path = ark_server_cfg_folder + "ark_server.cfg"


# ark_server.cfg
ark_server_cfg = """
[ArkServer]
CodeName = Mahjong
DatabaseName = Ark
RedisHost = dragon-redis-008-ark
RedisPort = 6379
MongoHost = 127.0.0.1
MongoPort = 27018
AutoID = 10000000
GMTTime = 8
CurrencyCode =CNY
LogLevel = INFO
MongoPoolSize = 30
RedisPoolSize = 30
SocketTimeout = 3
LoggerName = ErrorLog
CollName = ErrorLog

LicenseServer=http://172.32.128.14:8000/check
LicenseApp=dragon
LicenseKey= 1078bbc1ab497532dc79eb5c1bf7fc12
keyfile = generated-private-key.txt
certfile = gd_bundle-g2-g1.crt

[TableSystem]
RedisHost = dragon-fishredis-001-prod
RedisPort = 6379
RedisDB = 1

#Local lan ip mapping

"""
local_lan_ip_mapping = {
    Hostname._001:
        (
            "# {}".format(Hostname._001),
            "L52.220.110.233.5000 = 172.32.139.211:5000",
            "L52.220.110.233.5001 = 172.32.139.211:5001"
        ),
    Hostname._002:
        (
            "# {}".format(Hostname._002),
            "L52.220.152.100.5000 = 172.32.139.212:5000",
            "L52.220.152.100.5001 = 172.32.139.212:5001"
        ),
    Hostname._003:
        (
            "# {}".format(Hostname._003),
            "L52.221.41.214.5000 = 172.32.139.213:5000",
            "L52.221.41.214.5001 = 172.32.139.213:5001"
        ),
    Hostname._004:
        (
            "# {}".format(Hostname._004),
            "L52.74.78.111.5000 = 172.32.139.214:5000",
            "L52.74.78.111.5001 = 172.32.139.214:5001"

        ),
    Hostname._005:
        (
            "# {}".format(Hostname._005),
            "L52.76.14.40.5000 = 172.32.139.215:5000",
            "L52.76.14.40.5001 = 172.32.139.215:5001"
        ),
    Hostname._006:
        (
            "# {}".format(Hostname._006),
            "L52.77.173.166.5000 = 172.32.139.216:5000",
            "L52.77.173.166.5001 = 172.32.139.216:5001"
        ),
}


# 查看玩家是否都離線的資料庫連線設定
mongo_host = "mongo"
mongo_port = 28023
mongo_db_name = "Match"
mongo_collection_name = "MatchTable"
server_name_to_url_list = {
    Hostname._001: [
        "52.220.110.233:5000", "52.220.110.233:5001"
    ],
    Hostname._002: [
        "52.220.152.100:5000", "52.220.152.100:5001"
    ],
    Hostname._003: [
        "52.221.41.214:5000", "52.221.41.214:5001"
    ],
    Hostname._004: [
        "52.74.78.111:5000", "52.74.78.111:5001"
    ],
    Hostname._005: [
        "52.76.14.4:5000", "52.76.14.4:5001"
    ],
    Hostname._006: [
        "52.77.173.166:5000", "52.77.173.166:5001"
    ],
}
