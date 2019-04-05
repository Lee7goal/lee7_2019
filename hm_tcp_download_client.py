# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/5 0005 22:58'
__author__ = 'Lee7'
import socket


def main():
    # 创建socket
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取服务器信息
    dest_ip = input("输入IP")
    dest_port = int(input("输入端口"))
    # 连接服务器
    tcp_socket.connect((dest_ip, dest_port))
    # 输入需要下载的文件名
    download_file_name = input("请输入要下载的名字")

    # 发送下载请求
    tcp_socket.send(download_file_name.encode('utf-8'))
    # 接受对方发过来的数据，最大接受数据1024字节 1k
    recv_data = tcp_socket.recv(1024*1024)  # 1024--->1k 1024*1024--->1M 1024*1024*1024--->1G
    # print('接收到的数据为：',recv_data.decode('utf-8'))
    # 如果接收到数据再创建文件，否则不创建
    if recv_data:
        with open("【新】"+download_file_name,"wb") as f:
            f.write(recv_data)
    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
