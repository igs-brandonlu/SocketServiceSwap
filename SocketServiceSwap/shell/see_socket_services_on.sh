#!/usr/bin/env bash
# 检查是否在 Bash 中运行
if [ -z "$BASH_VERSION" ]; then
    echo "Please use bash instead of sh to run this script."
    exit 1
fi

if [ -z "$1" ]; then
    echo "dev/test/release : "
    read ENV
else
    ENV=$1
fi
cat "/etc/igs/Mahjong/Game/config/$ENV/ark_server.cfg" | grep -E -e 'L[0-9]+' -e 'dragon-'
