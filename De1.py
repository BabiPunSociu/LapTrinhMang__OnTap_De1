# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:28:35 2023

@author: ADMIN
"""

    # Ôn tập thi cuối kì

# Câu 1: Mô tả phương thức truyền dữ liệu theo giao thức TCP
# Câu 2: Viết chương trình đọc header của một trang web
# Câu 3: Xây dựng chương trình theo mô hình Client-Server sử dụng
#     socket theo giao thức TCP và thực hiện các công việc sau:
#     a, Client gửi tín hiệu kết nối đến server
#         - Cho phép người dùng nhập 1 chuỗi ký tự từ bàn phím
#         - Gửi chuỗi đã nhập đến server
#         - Nhận kết quả trả về
#     b, Server chấp nhận kết nối
#         - Nhận kết nối từ client, hiện thị thông tin client
#         - Nhận xâu ký tự từ client
#         - Đến số ký tự in hoa trong chuỗi
#         - Trả kết quả về cho client

    # LỜI GIẢI
#####################################################
# Câu 1:

#####################################################
# Câu 2:
import requests
# Tạo url
url = 'https://www.facebook.com'
# Tạo request HTTP Get
response = requests.get(url)
# Lấy dữ liệu header là dạng dictionary
headers = response.headers
# In nội dung của header
for key, value in headers.items():
    print(f'{key}: {value}')
#####################################################
# Câu 3:
#   --------------SERVER--------------
import socket
host = 'localhost'
port= 9050

def create_connect(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(5)
    print('Server san sang')
    return sk

def create_data(mes):
    data = mes + '\0'
    return data

def send_data(sk, mes):
    message = create_data(mes)
    sk.sendall(message.encode('utf-8'))

def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1: raise ConnectionError()
        data = data + data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def tinhSoChuCaiInHoa(chuoi):
    soluong = sum(1 for x in chuoi if x.isupper())
    return soluong

if __name__=='__main__':
    sk = create_connect(host, port)
    client_sk, client_addr = sk.accept()
    while True:
        # Nhan 1:
        message = recv_data(client_sk)
        print('Client: %s'%(message))
        if message == 'bye':
            client_sk.close()
            break
        # Gui 2
        soluong = tinhSoChuCaiInHoa(message)
        send_data(client_sk, str(soluong))
        print('Server: %d'%soluong)

#   --------------CLIENT--------------
# import socket
# host = 'localhost'
# port= 9050

# def create_connect(host, port):
#     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.bind((host, port))
#     sk.listen(5)
#     return sk

# def create_data(mes):
#     data = mes + '\0'
#     return data

# def send_data(sk, mes):
#     message = create_data(mes)
#     sk.sendall(message.encode('utf-8'))

# def recv_data(sk):
#     data = bytearray()
#     msg = ''
#     while not msg:
#         data1 = sk.recv(1024)
#         if not data1: raise ConnectionError()
#         data = data + data1
#         if b'\0' in data1:
#             msg = data.rstrip(b'\0')
#     msg = msg.decode('utf-8')
#     return msg

# if __name__=='__main__':
#     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.connect((host, port))
    
#     while True:
#         # Gui 1
#         message = input('Client:')
#         send_data(sk, message)
#         if message=='bye':
#             sk.close()
#             break
#         # Nhan 2
#         message = recv_data(sk)
#         print('Server: %s'%(message))