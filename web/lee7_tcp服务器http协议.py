# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/13 13:33'
__author__ = 'Lee7'
import socket


def service_client(new_client, clientaddr):
    # 接受浏览器发送的请求
    # GET /HTTP/1.1
    # ....
    # 接受对方发送的消息
    recv_data = new_client.recv(1024 * 1024 * 1024)  # 接受一个G
    print('接收到的数据为：\n', recv_data.decode('gbk'))
    # 准备HEADER
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 准备BODY
    response += "<h1>收到此消息代表连接成功</h1>"
    # 发送准备好的数据
    new_client.send(response.encode('gbk'))
    # 关闭套接字
    new_client.close()  # 关闭当前客户端连接u
    print("与 %s :%s端口连接断开" % (clientaddr[0], clientaddr[1]))


def main():
    """http回馈静态界面"""
    # 创建套接字
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 套接字绑定IP，PORT
    my_socket.bind(('127.0.0.1', 2333))
    # 开启监听
    my_socket.listen(128)
    print("服务器建立成功，等待连接...")
    while True:
        # 等待别人的连接
        new_client, clientaddr = my_socket.accept()
        print("与%s连接成功" % str(clientaddr[0]))
        # 为这个客户端服务
        service_client(new_client, clientaddr)

        print("等待下一个用户的连接")
    my_socket.close()  # 关闭监听服务器


if __name__ == "__main__":
    main()
