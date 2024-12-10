#!/usr/bin/python
#-*- encoding:utf8 -*-

import random
#本地生成一个文件，5000w行，每行内容为一个1亿以内的随机自然数

def random5kw(filename):
    with open(filename,'w') as file_out:
        for i in range(5000):
            one_random = random.randint(1,10000)
            file_out.write(str(one_random) + '\n')
            if (i+1)%100 == 0:
                print(filename,'lines',(i+1))


def distinct5kw(filename):
    tmp_dict = {}
    with open(filename,'r') as file_in:
        counting = 0
        for line in file_in:
            counting += 1
            one_random = int(line.strip())
            if one_random in tmp_dict:
                tmp_dict[one_random] += 1
            else:
                tmp_dict[one_random] = 1
            if counting % 100 == 0:
                print(counting)
    print(filename,'distinct count:',len(tmp_dict))
    return tmp_dict

def sort5kw(dict5kw,filename):
    with open(filename,'w') as file_out:
        for i in range(10000):
            if (i + 1) in dict5kw:
                one_line = str(i+1) +'\n'
                for j in range(dict5kw[i+1]):
                    file_out.write(one_line)
            if (i+1)%1000 == 0:
                print(filename,'sorting',i+1)
    print(filename,'sorted')

if __name__ == '__main__':
    random5kw('test01.txt')
    dict5kw = distinct5kw('test01.txt')
    sort5kw(dict5kw,'test02.txt')


