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

#遍历H1机下面的D1目录下近12个小时内生成的文件，把文件名写入列表中
def s_files(s_l):
    # 计算时间阈值，当前时间减去12小时
    time_threshold = time.time() - hours * 3600   
    s_recent_files = []
    for root,dirs,files in os.walk(s_l):
        for file in files:
            #获取文件路径
            file_path = os.path.join(root,file)
            #获取文件状态
            file_stat = os.stat(file_path)
            if file_stat.st_mtime > time_threshold:
                s_recent_files.append(file)
                #print(s_recent_files)
    return s_recent_files

#遍历H2机下面的D2目录下的所有文件，把文件名写入列表中
def t_files(t_ip,t_username,t_password,t_l):
    #创建了一个paramiko库中的SSHClient对象，名叫ssh
    ssh = paramiko.SSHClient()
    #调用SSHClient类的set_missing_host_key_policy方法
    #paramiko.AutoAddPolicy是paramiko提供的一种策略
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(t_ip, username=t_username, password=t_password)
        sftp = ssh.open_sftp()
        t_all_files = sftp.listdir(t_l)
        #print(t_all_files)
        """
        stdin,stdout,stderr = ssh.exec_command(f"ls{t_l}")
        file_names = stdout.read().decode().splitlines()
        t_all_files.extend(file_names)
        """
    except Exception as e:
        print(f"连接到H2服务机操作出现问题: {e}")
    finally:
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
    return t_all_files

#对比俩个列表之间的差距，如果相等，那么跳过，如果D1有的D2没有，那么把H1机的D1目录下面的文件复制到H2机D2目录下
def compare_copy_files(t_ip,s_l,t_l):
    s_files_list = s_files(s_l) 
    t_files_list = t_files(t_ip,t_username,t_password,t_l)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(t_ip,username=t_username,password=t_password)
        sftp = ssh.open_sftp()
        for s_i in s_files_list:
            if s_i not in t_files_list:
                s_file_path = os.path.join(s_l,s_i)
                l_file_path = os.path.join(t_l,s_i)
                l_file_path= l_file_path.replace("\\","/")
                print(s_file_path)
                print(l_file_path)
                sftp.put(s_file_path,l_file_path)
                print(f"{s_i}已经上传到H2_D2目录下")
            else:
                print(f"{s_i}在H2_D2目录下已经存在")
    except Exception as e:
        print(f"连接到H2服务机操作出现问题: {e}")
    finally:
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()

if __name__ == "__main__" :
    compare_copy_files(t_ip,s_l,t_l)
    #s_files(s_l)
    #t_files(t_ip,t_username,t_password,t_l)
  




   