# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/5 0005 20:57'
__author__ = 'Lee7'

from socket import *


def main():
    # 创建tcp_socket套接字
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    tcp_client_socket.bind(("",1888))
    # tcp_client_socket.listen(128)
    # 目的信息
    # sever_ip = input("请输入服务器IP：\n")
    # sever_port = int(input("请输入服务器PORT：\n"))
    # 连接服务器
    tcp_client_socket.connect(("192.168.0.106",3666))
    while True:
        #  提示用户输入数据
        send_data = input("请输入发送的信息: \n")
        tcp_client_socket.send(send_data.encode("utf-8"))

        #  接受对方发送的数据
        recv_data = tcp_client_socket.recv(1024)
        print("接受的数据为: %s" % (recv_data.decode('utf-8')))
    # 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()