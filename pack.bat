@echo off
REM 刪除現有的壓縮檔案
del /F /Q SocketServiceSwap.tar.gz

REM 創建新的壓縮檔案，排除 .log 和 .pyc 文件
tar -czvf SocketServiceSwap.tar.gz --exclude='*.log' --exclude='*.pyc' SocketServiceSwap
