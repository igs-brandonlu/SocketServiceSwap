#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

echo "dev/test/release : "
read ENV
case $ENV in
  dev)
    echo "您选择了开发环境 (dev)"
    bash ./ssh_t_to.sh "127.0.0.1" "cd ~/SocketServiceSwap/shell/; bash ./see_socket_services_on.sh $ENV;"
    ;;
  test)
    echo "您选择了测试环境 (test)"
    bash ./ssh_t_to.sh "dragon-mjsocket-002-test" "cd ~/SocketServiceSwap/shell/; bash ./see_socket_services_on.sh $ENV;"
    ;;
  release)
    echo "您选择了生产环境 (prod)"
    bash ./ssh_t_to.sh "dragon-mjgs-001-prod dragon-mjgs-002-prod" "cd ~/SocketServiceSwap/shell/; bash ./see_socket_services_on.sh $ENV;"
    ;;
  *)
    echo "无效的选项 请重新输入 dev/test/release"
    ;;
esac