import random
import time

start_time = time.time()

#本地生成一个文件，5000w行，每行内容为一个1亿以内的随机自然数
def generate_random_file():
    with open('random_number.txt','w') as file:
        for _ in range(5000):
            random_number = random.randint(1,10000)
            file.write(f"{random_number}\n")

#统计上述文件，去重后的行数是多少。
def count_distinct_lines():
    random_number_list = []
    with open('random_number.txt','r') as file:
        for i in file:
            if i not in random_number_list:
                random_number_list.append(i)
    print(len(random_number_list))

#将函数1的文件，进行排序。生成另一个文件。
def sorted_generate_random_file():
    random_number_list = []
    with open('random_number.txt','r') as file:
        for i in file:
            random_number_list.append(int(i))
        sort_random_number_list = sorted(random_number_list)

    with open('sorted_random_number.txt','w') as f:
        for i in sort_random_number_list:
            f.write(f'{i}\n')


if __name__ == "__main__":
    generate_random_file()
    count_distinct_lines()
    sorted_generate_random_file()

end_time = time.time()
print("耗时: {:.2f}秒".format(end_time - start_time))