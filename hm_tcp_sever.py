# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/5 0005 21:26'
__author__ = 'Lee7'


import socket


def main():
    # 创建tcp_socket套接字
    tcp_sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 插入绑定信息
    tcp_sever.bind(("",3666))
    # 将手机设置为正常的响铃模式
    tcp_sever.listen(128)
    print("服务器建立成功，等待连接...")
    # 等待别人的连接
    client_socket,clientAddr = tcp_sever.accept()
    print("与 ",str(clientAddr[0]),"连接成功")
    while True:
    # 接受对方发过来的数据
        print("等待对方发送消息...")
        recv_data = client_socket.recv(1024)  # 接受1024个字节
        print('接收到的数据为：',recv_data.decode('utf-8'))
        # 发送数据到客户端
        # send_msg = input("请输入回复信息，若无请按回车")
        client_socket.send("看到此条消息表示已经收到消息".encode('utf-8'))
    # 关闭套接字
    tcp_sever.close


if __name__ == "__main__":
    main()
