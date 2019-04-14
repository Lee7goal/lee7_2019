# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/14 0014 20:35'
__author__ = 'Lee7'
import socket
import re
import threading


def service_client(new_client, clientaddr):
    # 接受浏览器发送的请求
    # GET /HTTP/1.1
    # ....
    # 接受对方发送的消息
    recv_data = new_client.recv(1024 * 1024 * 1024).decode('utf-8')  # 接受一个G
    # print('----------------->接收到的数据为：\n%s' % recv_data)
    request_lines = recv_data.splitlines()
    print("")
    print(">"*20)
    print(request_lines)
    # GET /index.html HTTP/1.1
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"
    try:
        # 准备BODY
        f = open("./html" + file_name, "rb+")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "<html><head>NOT FOUND</head><body><h1>-------file not found-------</h1></body></html>"
        new_client.send(response.encode('utf-8'))
    else:
        content = f.read()
        f.close()
        # 准备HEADER
        response = "HTTP/1.1 200 OK Content-Type: text/html;charset=utf-8\r\n"
        response += "\r\n"
        # 发送准备好的HEADER
        new_client.send(response.encode('utf-8'))
        # 发送准备好的BODY
        new_client.send(content)

    # 关闭套接字
    new_client.close()  # 关闭当前客户端连接u
    print("与 %s :%s端口连接断开" % (clientaddr[0], clientaddr[1]))


def main(port):
    """
    http回馈静态界面\n
    :port 填写一个端口号
    """
    # 创建套接字
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close时服务器4次挥手之后资源能够立即释放，这样就保证了下次运行程序是，可以立即使用
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 套接字绑定IP，PORT
    my_socket.bind(('127.0.0.1', port))
    # 开启监听
    my_socket.listen(128)
    print("服务器建立成功，等待连接...")
    while True:
        # 等待别人的连接
        new_client, clientaddr = my_socket.accept()
        print("与%s连接成功" % str(clientaddr[0]))
        # 为这个客户端服务
        t1 = threading.Thread(target=service_client, args=(new_client, clientaddr))
        t1.start()
        print("等待下一个用户的连接")


if __name__ == "__main__":
    main(3501)
