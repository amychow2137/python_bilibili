####
# 跨主机文件传输
# 1.有两台 Linux主机，主机H1和 H2;
# 2.指定 H1的目录D1下，所有文件生成时间在最近12小时内的文件，复制传输到H2的目录 D2;
# 3.如果在 D2 目录下，已经有同名文件了，则不需要传输。
# 4.Python 程序放在H1下，参数有3个，分别是H1、H2 的IP和 D2
# 5.用 paramiko 模块
# 以上程序重复跑批，则能够陆续将文件传输到 D2 目录，仅需要传输一次，节省重复覆盖的工作。一些其他信息
# H1 是 10.101.21.97
# H2 是 10.101.21.103
# D1是/report_shared/Rpt2nd_nsz/ D2是/newweb/report/usz_upload/
# 开发的时候，参数可以变于是可以自行设置test来测试
##

import os
import paramiko
import datetime
import time

D1 = "/Users/yorikhu/Desktop/temp/data"
D2 = "/test_source"


# Infer file in time
def isTimeInHours(timeParam):
    hours = 12
    time_threshold = time.time() - hours * 3600
    return timeParam > time_threshold


# Connect H2
def connect_remote_server(h2_ip):
    # Create SSHClient
    ssh = paramiko.SSHClient()
    # No know_hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect H1 or H2 ip: 106.12.161.89
    ssh.connect(h2_ip, username="root", password="@Yq991008hyq")
    sftp = ssh.open_sftp()
    return [ssh, sftp]


# Disconnect H2
def disconnect_remote_server(entity_list):
    ssh, sftp = entity_list
    if sftp:
        sftp.close()
    if ssh:
        ssh.close()
    return


# H1 local files
def get_local_files(d1_url):
    file_list = []

    for root, dirs, files in os.walk(d1_url):
        for file in files:
            # Get file base_url
            file_path = os.path.join(root, file)
            # Get file state
            file_stat = os.stat(file_path)
            # Infer time
            if isTimeInHours(file_stat.st_mtime):
                file_list.append(file)

    return file_list


# H2 remote files
def get_remote_files(sftp, d2_url):
    return sftp.listdir(d2_url)


# Compare
def compare_files_diff(d1_file_list, d2_file_list):
    diff_list = []
    for file in d1_file_list:
        if file not in d2_file_list:
            diff_list.append(file)
    return diff_list


# Send files to remote server
def send_files_to_remote_server(diff_list, sftp, d1_url, d2_url):
    for diff_name in diff_list:
        sftp.put(f"{d1_url}/{diff_name}", f"{d2_url}/{diff_name}")

    print(f"成功上传/更新了 {len(diff_list)} 个文件！")
    return


# main
def sync_files(H1_ip, H2_ip, d1_url, d2_url):
    try:
        entity_list = connect_remote_server(H2_ip)
        ssh, sftp = entity_list

        d1_file_list = get_local_files(d1_url)

        d2_file_list = get_remote_files(sftp, d2_url)

        diff_list = compare_files_diff(d1_file_list, d2_file_list)

        send_files_to_remote_server(diff_list, sftp, d1_url, d2_url)

    except Exception as e:
        print("ERROR：" + e)

    finally:
        disconnect_remote_server(entity_list)


if __name__ == "__main__":
    sync_files("local", "106.12.161.89", D1, D2)
