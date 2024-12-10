import os
import fnmatch
directory_path = "C:\\Users\\Administrator\\Desktop\\python\\tools\\check"

def check_length_add(txtname,dicname):
#获取chec.txt文件里面的文件名字，并且匹配s25目录下的文件,
#获取匹配到的对应文件名字得到第一行的len
    files = os.listdir(dicname)
    #print(files)
    length_list = []
    with open(txtname,'r') as f:
        for i in f.readlines():
            sheetname = i.split("|")[0]
            for x in files:
                if fnmatch.fnmatch(x,f"*{sheetname}*"):
                    file_path = os.path.join(directory_path+"\\s25",x)
                    with open(file_path,"r+") as fff:
                        line = fff.readline()
                        length = len(line)
                        length_list.append(length)
    return length_list

def write_length(txtname,dicname):
    write_length_list = []
    length_list = check_length_add(txtname,dicname)
    #print(length_list)
    with open(txtname,"r+") as n:
        lines = n.readlines()
        print(lines)
        num = 0
        for l in lines:
            #for i in length_list:
            write_length_list.append(l.replace("\n","")+f"|{length_list[num]}\n")      
            num +=1
    #print(write_length_list)
    return write_length_list

def write_file(txtname,dicname):
    write_length_list1 = write_length(txtname,dicname)
    with open(txtname,'w') as f:
        f.write("".join(write_length_list1))

if __name__ == "__main__":
    write_file("check.txt","s25")
    #write_length("check.txt","s25")

                
         

