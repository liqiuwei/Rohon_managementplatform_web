import socket
import json

from middleware.heandler import Hadnler

logging = Hadnler.logger


class TCPClient(object):
    """用于测试socket请求"""

    def __init__(self, domain, port, timeout=30, max_receive=102400):
        self.domain = domain
        self.port = port
        self.connected = 0  # 连接后置为1
        self.max_receive = max_receive
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(timeout)

    def connect(self):
        """连接指定IP、端口"""
        if not self.connected:
            try:
                self._sock.connect((self.domain, self.port))
            except socket.error as e:
                logging.exception(e)
            else:
                self.connected = 1
                logging.debug('TCPClient connect to {0}:{1} success.'.format(self.domain, self.port))

    def send(self, data, dtype='str', suffix=''):
        """向服务器端发送send_string，并返回信息，若报错，则返回None"""
        if dtype == 'json':
            send_string = json.dumps(data) + suffix
        else:
            send_string = data + suffix
        self.connect()
        if self.connected:
            try:
                self._sock.send(send_string.encode())
                logging.debug('TCPClient Send {0}'.format(send_string))
            except socket.error as e:
                logging.exception(e)

            try:
                rec = self._sock.recv(self.max_receive).decode()
                if suffix:
                    rec = rec[:-len(suffix)]
                logging.debug('TCPClient received {0}'.format(rec))
                return rec
            except socket.error as e:
                logging.exception(e)

    def close(self):
        """关闭连接"""
        if self.connected:
            self._sock.close()
            logging.debug('TCPClient closed.')


##########################################以下是测试用例调用上面的socket接口#######################################
#
import unittest






class TestAdd(unittest.TestCase):

    def setUp(self):
        ip = '192.168.1.146'
        port = 40001
        self.client = TCPClient(ip, port)

    def tearDown(self):
        self.client.close()

    def test_add(self):
        data = {
            'action': '1',
            # 'params': {'a': 1, 'b': 2}
        }
        res = self.client.send(data, dtype='json')
        print(res)
        # self.assertEqual(res, 3)
        # self.assertEqual(res, 'add')

    # def test_wrong_action(self):
    #     data = {
    #         'action': 'sub',
    #         'params': {'a': 1, 'b': 2}
    #     }
    #     res = self.client.send(data, dtype='json')
    #     self.assertEqual( res, -2)
    #     self.assertEqual( res, 'Wrong Action')

    # def test_wrong_data(self):
    #     data = 'xxxxx'
    #     res = self.client.send(data)
    #     self.assertEqual(je.extract('code', res), -1)
    #     self.assertEqual(je.extract('message', res), 'Data Error')
    #

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()

# #######################简单的发送coket数据#####################################
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('192.168.1.146', 40001))
# import time
#
# flag = '1'
#
# while True:
#     time.sleep(3)
#     print('send to server with value: ' + flag)
#     sock.send(flag.encode())
#     print(sock.recv(1024))
#     flag = (flag == '1') and '2' or '1'  # change to another type of value each time
#     sock.close()