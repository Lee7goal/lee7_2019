# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/4 0004 21:34'
__author__ = 'Lee7'
import socket
def main():
    # 1.打开套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("192.168.0.106",5555))
    print("开启接受成功，等待消息...")
    # dest_ip = input("请输入对方的IP")
    # dest_port = int(input("请输入对方的"))
    # 2.使用收发
    while True:
        get_text = udp_socket.recvfrom(1024)
        print("【FROM】%s \n %s" % (get_text[1],get_text[0].decode("utf-8")))
        send_msg = input("请输入回复的信息\n")
        udp_socket.sendto(send_msg.encode("utf-8"),get_text[1])
    # 3.关闭套接字
    udp_socket.close()
if __name__ == "__main__":
    main()