import paramiko
import os
import time

#s_ip = "10.101.21.97" #H1
t_ip = "106.12.161.89" #H2
s_l = r"C:\Users\Administrator\Desktop\D1" #H1的该目录下的D1目录下
t_l = r"/test_source" #H2的该目录下的D2目录下
hours = 12
t_username = "root"
t_password = "@Yq991008hyq"

#连接
def connect(t_ip,t_username,t_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(t_ip, username=t_username, password=t_password)
    sftp = ssh.open_sftp()
    return[ssh,sftp]

#退出连接
def close_connect(ssh,sftp):
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
        return


#遍历H1机下面的D1目录下近12个小时内生成的文件，把文件名写入列表中
def s_files(s_l):
    time_threshold = time.time() - hours * 3600   
    s_recent_files = []
    for root,dirs,files in os.walk(s_l):
        for file in files:
            file_path = os.path.join(root,file)
            file_stat = os.stat(file_path)
            if file_stat.st_mtime > time_threshold:
                s_recent_files.append(file)
    return s_recent_files

#遍历H2机下面的D2目录下的所有文件，把文件名写入列表中
def t_files(sftp,t_l):
        return sftp.listdir(t_l)
  
#main
#对比俩个列表之间的差距，如果相等，那么跳过，如果D1有的D2没有，那么把H1机的D1目录下面的文件复制到H2机D2目录下
def compare_copy_files(t_ip,s_l,t_l):
    try:
        connect_list = connect(t_ip,t_username,t_password)
        ssh,sftp = connect_list

        s_files_list = s_files(s_l) 

        t_files_list = t_files(sftp,t_l)

        for s_i in s_files_list:
            u_count = 0
            e_count = 0
            if s_i not in t_files_list:
                u_count =+ 1
                s_file_path = os.path.join(s_l,s_i)
                l_file_path = os.path.join(t_l,s_i).replace("\\","/")
                sftp.put(s_file_path,l_file_path)
                print(f"{s_i}Successfully Uploaded,COUNT:{u_count}")
            else:
                e_count =+ 1
                print(f"{s_i}Already Exist,COUNT:{e_count}")

    except Exception as e:
        print(f"compare_copy_filesError: {e}")

    finally:
        close_connect(ssh,sftp)
         

if __name__ == "__main__" :
    compare_copy_files(t_ip,s_l,t_l)




   