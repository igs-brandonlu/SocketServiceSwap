#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

# 獲得python腳本的路徑
cd ~/SocketServiceSwap/shell/
PY_SCRIPT_PATH="../python"
# 獲得機器名稱
HOSTNAME=$(hostname)
printf "機器名稱是: $HOSTNAME\n"

# 看看要移出/移入服務的機器
msg="$HOSTNAME \n"
output=$(python $PY_SCRIPT_PATH/check_config.py move_out)
msg+="移出: $output \n"
output=$(python $PY_SCRIPT_PATH/check_config.py move_in)
msg+="移入: $output \n"
printf -e "$msg\n"
python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
sleep 3

# 寫入ark_server.cfg
output=$(python $PY_SCRIPT_PATH/save_config.py)
printf "$HOSTNAME save_config.py 的輸出是: $output\n"

if [ "$output" = "success" ]; then
  msg="成功寫入 ark_server.cfg"
  printf "$msg\n"
  python $PY_SCRIPT_PATH/send_telegram_message.py "$HOSTNAME $msg"
  sleep 3
else
  msg="寫入 ark_server.cfg 失敗"
  printf "$msg\n"
  python $PY_SCRIPT_PATH/send_telegram_message.py "$HOSTNAME $msg"
  sleep 3
  exit 1
fi
sleep 3

# 重啟配桌服務
printf "重啟配桌服務...\n"
systemctl restart igsMahjong_Game.service
msg="重啟配桌服務完成"
printf "$msg\n"
python $PY_SCRIPT_PATH/send_telegram_message.py "$HOSTNAME $msg"
sleep 3
