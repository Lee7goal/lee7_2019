# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/16 15:03'
__author__ = 'Lee7'
import socket
import time

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("127.0.0.1", 2333))
tcp_server.listen(128)
tcp_server.setblocking(False)  # 设置为非堵塞方式
client_socket_list = list()
while True:
    time.sleep(1)
    try:
        new_socket, new_addr = tcp_server.accept()
    except Exception as ret:
        print("没有新的客户端到来")
    else:
        print("有一个新的客户端到来")
        new_socket.setblocking(False)  # 设置为非堵塞方式
        client_socket_list.append(new_socket)
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024).decode('gbk')
        except Exception as ret:
            print("没有发送过来数据")
        else:
            if recv_data:
                # 对方发送过来了数据
                print("收到了数据:\n %s" % recv_data)
                response = "HTTP/1.1 200 OK\r\n"
                response += "\n"
                response += "<h1>hahahahaha</h1>"
                client_socket.send(response.encode('gbk'))
            else:
                # 对方调用了close,导致了recv返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("客户端已经关闭")
