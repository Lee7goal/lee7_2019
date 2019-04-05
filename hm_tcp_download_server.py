# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/5 0005 22:33'
__author__ = 'Lee7'


import socket


def send_file_2_client(client_socket, clientaddr):
    # 1.接受客户端发送过来的要下载的文件名
    file_name = client_socket.recv(1024)  # 接受1024个字节
    print("客户端需要下载的文件是 %s " % file_name)
    file_content = None
    # 2.打开这个文件并读取内容
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:  # 只有一种异常，打不开
        print("没有要下载的文件(%s)" % file_name)
    # 3.发送文件的数据到客户端
    if file_content:
        client_socket.send(file_content)


def main():
    """循环为多个客户端服务器,并且多次服务一个客户端"""
    # 1.创建tcp_socket套接字
    tcp_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.插入绑定信息
    tcp_sever.bind(("", 6666))
    # 3.将手机设置为正常的响铃模式
    tcp_sever.listen(128)
    print("服务器建立成功，等待连接...")
    while True:
        # 4.等待别人的连接
        client_socket, clientaddr = tcp_sever.accept()
        print("与 %s :%s 端口连接成功" % (clientaddr[0], clientaddr[1]))
        # 5.调用发送文件函数，完成为客户端服务
        send_file_2_client(client_socket, clientaddr)
        print("发送成功!")
        # 6.关闭当前客户端连接
        client_socket.close()
        print("与 %s :%s端口连接断开" % (clientaddr[0], clientaddr[1]))
        print("等待下一个用户的连接")
    tcp_sever.close()  # 关闭整个服务器


if __name__ == "__main__":
    main()
