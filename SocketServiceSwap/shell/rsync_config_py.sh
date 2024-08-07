#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

# 檢查是否有提供參數
if [ -z "$1" ]; then
    echo "dev/test/prod : "
    read ENV
else
    ENV=$1
fi
case $ENV in
    dev)
        echo "您选择了开发环境 (dev)"
        rsync -avz ~/SocketServiceSwap/python/config.py igs@127.0.0.1:~/SocketServiceSwap/python/config.py
        ;;
    test)
        echo "您选择了测试环境 (test)"
        rsync -avz ../python/config.py dragon-mjgs-002-test:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-002-test:~/SocketServiceSwap/python/config.py
        ;;
    prod)
        echo "您选择了生产环境 (prod)"
        rsync -avz ../python/config.py dragon-mjgs-001-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjgs-002-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-001-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-002-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-003-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-004-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-005-prod:~/SocketServiceSwap/python/config.py
        rsync -avz ../python/config.py dragon-mjsocket-006-prod:~/SocketServiceSwap/python/config.py
        ;;
    *)
        echo "无效的选项，请输入 dev、test 或 prod"
        ;;
esac
