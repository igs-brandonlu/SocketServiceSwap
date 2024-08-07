# coding: utf-8

import os, traceback
from config import move_out, move_in, ark_server_cfg_folder, ark_server_cfg_path, build_config
from logger import get_logger


def main(logger):
    try:
        cfg_txt = build_config(move_in_list=move_in, move_out_list=move_out)

        if not os.path.exists(ark_server_cfg_folder):
            # 确保路径存在，递归创建目录
            os.makedirs(os.path.dirname(ark_server_cfg_path))
        # 寫入設定檔
        with open(ark_server_cfg_path, 'w') as f:
            f.write(cfg_txt)
        return "success"
    except:
        logger.error(traceback.format_exc())
        return "fail"


if __name__ == "__main__":
    logger = get_logger('save_config')
    result = main(logger)
    print(result)
