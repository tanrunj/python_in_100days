from time import time
from threading import Thread

import requests

# request and thread download image
class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)

        with open('./' + filename, 'wb') as f:
            f.write(resp.content)

def main_request():

    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=fd9e384154ab247a39fbc0e832c79e0d&num=5'
    )

    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()


# Socket Single I/O
from socket import socket, SOCK_STREAM, AF_INET, AF_INET6
from datetime import datetime

def main_single():
    # define socket type
    # family=AF_INET IPv4
    # family=AF_INET6 IPv6
    # type=SOCK_STREAM TCP
    # type=SOCK_DGRAM UDP
    # type=SOCK_RAW 原始
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('172.20.10.2', 8001))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('server start listening')
    while True:
        client, addr = server.accept()
        print(str(addr) + 'connect to server.')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


# Socket Multiple I/O
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)

            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('172.20.10.2', 8001))
    server.listen(512)
    print('server start listening.')
    with open('guido.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()