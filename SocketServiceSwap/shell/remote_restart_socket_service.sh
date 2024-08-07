#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

echo "dev/test/prod : "
read ENV

# 獲得python腳本的路徑
cd ~/SocketServiceSwap/shell/
PY_SCRIPT_PATH="../python"
## 查看config.py
#ARGV="see_restart_config"
#OUTPUT=$(python $PY_SCRIPT_PATH/config.py $ARGV)
#echo $OUTPUT
echo "同步config.py到遠端? (y/n)"
read YES_OR_NO
case $YES_OR_NO in
    y)
        echo "同步config.py到遠端..."
        bash ./rsync_config_py.sh $ENV
        echo "完成"
        ;;
    n)
        echo "不同步config.py到遠端"
        ;;
    *)
        echo "無效的選項，請輸入 y 或 n"
        exit 1
        ;;
esac

echo "sudo password: "
read -s PASSWORD
case $ENV in
    dev)
        echo "您选择了开发环境 (dev)"
        bash ./ssh_t_to.sh "127.0.0.1" "cd ~/SocketServiceSwap/shell/; echo $PASSWORD| sudo -S sh ./restart_socket_service.sh"
        ;;
    test)
        echo "您选择了测试环境 (test)"
        bash ./ssh_t_to.sh "dragon-mjsocket-002-test" "cd ~/SocketServiceSwap/shell/; echo $PASSWORD| sudo -S sh ./restart_socket_service.sh"
        ;;
    prod)
        echo "您选择了生产环境 (prod)"
        bash ./ssh_t_to.sh "dragon-mjsocket-001-prod dragon-mjsocket-002-prod dragon-mjsocket-003-prod dragon-mjsocket-004-prod dragon-mjsocket-005-prod dragon-mjsocket-006-prod" "cd ~/SocketServiceSwap/shell/; echo $PASSWORD| sudo -S sh ./restart_socket_service.sh"
        ;;
    *)
        echo "无效的选项，请输入 dev、test 或 prod"
        ;;
esac
