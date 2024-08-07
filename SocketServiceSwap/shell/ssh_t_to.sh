#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

# HOSTS_LIST: Server list
HOSTS_LIST=$1
CMD=$2

echo "--------------------------------------------------------"
echo "ssh to server, $HOSTS_LIST "
echo "CMD is $CMD "
echo "--------------------------------------------------------"

for i in $HOSTS_LIST
do
  CONNECT_TIMEOUT=5
  TARGET_HOST="$i"
  TARGET_PORT=22  # SSH 默認端口
  echo "Testing connection to $TARGET_HOST on port $TARGET_PORT..."
  timeout $CONNECT_TIMEOUT nc -zv $TARGET_HOST $TARGET_PORT
  RESULT=$?
  if [ $RESULT -eq 0 ]; then
    echo "Connection successful. Executing SSH command..."

    echo "ssh to $TARGET_HOST $CMD"
    ssh -t $TARGET_HOST $CMD
    echo "Done."

  else
    echo "Connection $TARGET_HOST timed out after $CONNECT_TIMEOUT seconds. Aborting SSH command."
  fi
done
