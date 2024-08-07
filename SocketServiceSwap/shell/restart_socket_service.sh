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
echo "機器名稱是: $HOSTNAME"

# 確認這台是否被設定為要移出的服務
output=$(python $PY_SCRIPT_PATH/is_need_restart_socket.py $HOSTNAME)
echo "這台是否移出服務?: $output"
if [ "$output" = "yes" ]; then
  echo "$HOSTNAME 是。必須等人數歸零後重啟服務"
else
  echo "$HOSTNAME 否。結束"
  exit 0
fi

# 檢查移出配桌的socket伺服器服務，目前人數是否歸零，如是則重啟服務
player_count=$(python $PY_SCRIPT_PATH/check_player_online_count.py)
if [ "$player_count" -le -1 ]; then
  msg="$HOSTNAME 不需要重啟服務，結束。"
  echo $msg
  python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
  sleep 3
  exit 0
fi

msg="$HOSTNAME 目前人數: $player_count"
echo $msg
python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
sleep 3
# 檢查人數歸零 sleep 時間
SLEEP_TIME=30
SLEEP_TIME_MAX=300
while [ "$player_count" -gt 0 ]; do
  msg="$HOSTNAME 等待人數歸零，目前人數: $player_count"
  echo $msg
  python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
  sleep $SLEEP_TIME
  SLEEP_TIME=$((SLEEP_TIME + 30))
  if [ "$SLEEP_TIME" -gt "$SLEEP_TIME_MAX" ]; then
    SLEEP_TIME=$SLEEP_TIME_MAX
  fi

  # 更新 player_count 的值
  player_count=$(python $PY_SCRIPT_PATH/check_player_online_count.py)
done

msg="$HOSTNAME 所有玩家已下線，服務即將重啟"
echo $msg
python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
sleep 3
# 在這裡添加重啟服務的命令，例如：sudo systemctl restart your_service
echo "重啟服務..."
systemctl restart igsMahjong_GameSocket.service
msg="$HOSTNAME 重啟服務完成"
echo $msg
python $PY_SCRIPT_PATH/send_telegram_message.py "$msg"
sleep 3
