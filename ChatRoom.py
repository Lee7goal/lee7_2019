# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/4 0004 22:47'
__author__ = 'Lee7'
import socket


def main():
    #  创建套接字
    loyo_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #  绑定自身ip及端口
    local_ip = input("请输入本机IP：\n")
    local_port = int(input("请输入本机PORT：\n"))
    loyo_socket.bind((local_ip,local_port))
    #  设定对方IP及端口
    dest_ip = input("请输入对方IP：\n")
    dest_port = int(input("请输入对方PORT："))
    dest_addr = (dest_ip,dest_port)
    #  循环来进行处理事情
    while True:
        #  发送
        send_msg = input("请输入发送内容：\n")
        loyo_socket.sendto(send_msg.encode("utf-8"),dest_addr)
        #  接受并显示
        recv_msg = loyo_socket.recvfrom(1024)
        print("【FROM】%s \n%s" % (recv_msg[1],recv_msg[0].decode("utf-8")))

    #  关闭套接字
    loyo_socket.close()


if __name__ == "__main__":
    main()
