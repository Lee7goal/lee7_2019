# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 21:01'
__author__ = 'Lee7'
import socket
import threading


def send_msg(client_socket, dest_ip, dest_port):
    # 启动收函数
    while True:
        send_data = input("输入要发送的内容：")
        client_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(client_socket):
    # 启动发函数
    while True:
        recv_data = client_socket.recvfrom(1024)
        print("【来自】%s :\n%s" % (recv_data[1], recv_data[0].decode('utf-8')))


def main():
    """多任务udp聊天器"""
    # 创建套接字并绑定
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_port = int(input("选择一个PORT："))
    client_socket.bind(("", local_port))
    dest_ip = input("请输入对方的IP")
    dest_port = int(input("请输入对方的端口"))
    # 创建两个线程，执行相应功能
    t1 = threading.Thread(target=recv_msg, args=(client_socket,))
    t2 = threading.Thread(target=send_msg, args=(client_socket, dest_ip, dest_port))
    # 启动线程
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
