# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/4 0004 22:47'
__author__ = 'Lee7'
import socket


def send_mesg(loyo_socket):
    """发送消息"""
    #  设定对方IP及端口
    dest_ip = input("请输入对方IP：\n")
    dest_port = int(input("请输入对方PORT："))
    dest_addr = (dest_ip, dest_port)
    #  发送
    send_msg = input("请输入发送内容：\n")
    loyo_socket.sendto(send_msg.encode("gbk"), dest_addr)


def recv_mesg(loyo_socket):
    #  接受并显示
    recv_msg = loyo_socket.recvfrom(1024)
    print("【FROM】%s \n%s" % (str(recv_msg[1]), recv_msg[0].decode("gbk")))


def main():
    #  创建套接字
    loyo_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    loyo_socket.bind(("",7788))

    #  循环来进行处理事情
    while True:
        print("-----Loyo聊天室-----")
        print("1：发送消息")
        print("2：接受消息")
        print("0：退出系统")
        op = input("请选择功能：")
        if op == "1":
            # 发送
            send_mesg(loyo_socket)
        elif op == "2":
            # 接受
            recv_mesg(loyo_socket)
        elif op == "0":
            print("退出成功，销毁数据")
            quit()
        else:
            print("输入有误请重新输入")

#  关闭套接字
    loyo_socket.close()


if __name__ == "__main__":
    main()
