#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

echo "dev/test/prod : "
read ENV
case $ENV in
    dev)
        echo "您选择了开发环境 (dev)"
        ssh -t igs@127.0.0.1 "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ igs@127.0.0.1:~/SocketServiceSwap/
        ;;
    test)
        echo "您选择了测试环境 (test)"
        ssh -t dragon-mjgs-002-test "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjgs-002-test:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-002-test "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-002-test:~/SocketServiceSwap/
        ;;
    prod)
        echo "您选择了生产环境 (prod)"
        ssh -t dragon-mjgs-001-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjgs-001-prod:~/SocketServiceSwap/

        ssh -t dragon-mjgs-002-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjgs-002-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-001-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-001-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-002-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-002-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-003-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-003-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-004-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-004-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-005-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-005-prod:~/SocketServiceSwap/

        ssh -t dragon-mjsocket-006-prod "cd ~; mkdir -p SocketServiceSwap/shell/ SocketServiceSwap/python/ SocketServiceSwap/python/template/dev/ SocketServiceSwap/python/template/test/ SocketServiceSwap/python/template/prod/"
        rsync -avz --exclude='__pycache__' --exclude='*.log' --exclude='*.pyc' ../ dragon-mjsocket-006-prod:~/SocketServiceSwap/
        ;;
    *)
        echo "无效的选项，请输入 dev、test 或 prod"
        ;;
esac
