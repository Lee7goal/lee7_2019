# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/5 0005 22:33'
__author__ = 'Lee7'


import socket


def main():
    """循环为多个客户端服务器,并且多次服务一个客户端"""
    # 创建tcp_socket套接字
    tcp_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 插入绑定信息
    tcp_sever.bind(("", 3888))
    # 将手机设置为正常的响铃模式
    tcp_sever.listen(128)
    print("服务器建立成功，等待连接...")
    while True:
        # 等待别人的连接
        client_socket, clientaddr = tcp_sever.accept()
        print("与 %s :%s 端口连接成功" % (clientaddr[0], clientaddr[1]))
        while True:
            # 接受对方发过来的数据
            print("等待对方发送消息...")
            recv_data = client_socket.recv(1024)  # 接受1024个字节
            print('接收到的数据为：', recv_data.decode('gbk'))
            # 发送数据到客户端
            if recv_data:
                # send_msg = input("请输入回复信息，若无请按回车")
                client_socket.send("看到此条消息表示已经收到消息\n如需退出请回复空".encode('gbk'))
            else:
                break
            # 关闭套接字
        # if recv_data.decode('gbk') == "退出":
        client_socket.close()  # 关闭当前客户端连接
        print("与 %s :%s端口连接断开" % (clientaddr[0], clientaddr[1]))
        print("等待下一个用户的连接")
    tcp_sever.close()  # 关闭整个服务器


if __name__ == "__main__":
    main()
