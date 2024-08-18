# coding: utf-8

import sys

ENVIRONMENT = "prod"  # "dev"  # "test"  # "prod"
if ENVIRONMENT == "dev":
    from template.dev.config import *
elif ENVIRONMENT == "test":
    from template.test.config import *
elif ENVIRONMENT == "prod":
    from template.prod.config import *
else:
    raise ValueError("Unknown environment: {}".format(ENVIRONMENT))


# 要移出的機器
move_out = [
    Hostname._004, Hostname._005, Hostname._006
]

# 要移入的機器
move_in = [
    Hostname._001, Hostname._002, Hostname._003
]

# 要重啟的機器
restart_socket = [
    Hostname._004
]


def get_server_url_list(server_name_list):
    final_server_url_list = list()
    for server_name in server_name_list:
        server_url_list = server_name_to_url_list.get(server_name, [])
        for url in server_url_list:
            final_server_url_list.append(url)
    return final_server_url_list


def build_config(move_in_list, move_out_list):
    local_lan_ip_mapping_txt = ""
    for server in move_in_list:
        if server in local_lan_ip_mapping:
            # 註釋
            local_lan_ip_mapping_txt += local_lan_ip_mapping[server][0] + "\n"
            # service port 0
            local_lan_ip_mapping_txt += local_lan_ip_mapping[server][1] + "\n"
            # service port 1
            if len(local_lan_ip_mapping[server]) >= 3:
                local_lan_ip_mapping_txt += local_lan_ip_mapping[server][2] + "\n"
    local_lan_ip_mapping_txt += "\n"
    for server in move_out_list:
        if server in local_lan_ip_mapping:
            # 註釋
            local_lan_ip_mapping_txt += local_lan_ip_mapping[server][0] + "\n"
            # service port 0
            local_lan_ip_mapping_txt += "# " + local_lan_ip_mapping[server][1] + "\n"
            # service port 1
            if len(local_lan_ip_mapping[server]) >= 3:
                local_lan_ip_mapping_txt += "# " + local_lan_ip_mapping[server][2] + "\n"
    local_lan_ip_mapping_txt += "\n"

    final_cfg = str(ark_server_cfg) + "\n" + local_lan_ip_mapping_txt
    return final_cfg


def see_swap_config():
    print("要移出的機器:")
    print(move_out)
    print("要移入的機器:")
    print(move_in)


def see_restart_config():
    print('要重啟的機器:')
    print(restart_socket)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        pass
    elif sys.argv[1] == "see_swap_config":
        see_swap_config()
    elif sys.argv[1] == "see_restart_config":
        see_restart_config()
    else:
        print("Unknown argv: {}".format(sys.argv[1]))
