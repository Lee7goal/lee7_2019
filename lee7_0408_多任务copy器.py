# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/8 16:14'
__author__ = 'Lee7'
import multiprocessing
import os


def copy_file(q,file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("------->模拟拷贝文件：从%s----->到%s,文件名是: %s" % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name,"rb")  # 拼接路径
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + "/" + file_name,"wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，就向队列put一个消息，表示完成
    q.put(file_name)

    
def main():
    # 1.获取要copy的文件夹的名字
    old_folder_name = input("请输入要copy的名字")
    # 2.创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "【复件】"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3.获取文件夹的所有待copy的名字 listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 4.创建进程池
    po = multiprocessing.Pool(5)

    # 5..创建一个队列
    q = multiprocessing.Manager().Queue()
    # 6.向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q,file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测一下文件个数
    copy_complete = 0
    while True:
        file_name = q.get()
        # print("已经完成COPY：%s" % file_name)
        copy_complete += 1
        a = copy_complete/all_file_num*100
        print("已经拷贝%.2f %%" % a)

        if copy_complete >= all_file_num:
            break
    # 5.复制原文件夹中的文件，到新的文件夹去
if __name__ == "__main__":
    main()
