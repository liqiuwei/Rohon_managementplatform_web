# import socket
# import time
# import threading
#
#
# class Client:
#     def __init__(self,host,port):
#         self.port = port
#         self.host = host
#         self.status = 0
#         self.BUF_SIZE = 1024
#
#     def connect(self):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 在客户端开启心跳
#         self.client.connect((self.host, self.port))
#
#     def send(self,mes):
#         client.startResv()
#         while True:
#             self.client.send(mes.encode())
#             time.sleep(1)  # 如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点
#
#     def resv(self):
#         while True:
#             data = self.client.recv(self.BUF_SIZE)
#             text = data.decode()
#             print(text)
#
#     def startResv(self):
#         t = threading.Thread(target=self.resv)
#         t.start()
#
#     def close(self):
#         self.client.close()
#
#
# if __name__ == "__main__":
#     client = Client("localhost",8083)
#     client.connect()
#     client.send("hello")

############################################################################################################

# python 模拟服务器发送socket消息
# import socket
# import time
# class Server:
#     def __init__(self, host, port):
#         self.port = port
#         self.host = host
#         self.status = 0
#         self.BUF_SIZE = 1024
#
#     def createServer(self):
#         self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server.bind((self.host, self.port))
#
#     def startServer(self):
#         self.status = 1
#         self.createServer()
#         # 设置接收的连接数为1
#         self.server.listen(1)
#         client, address = self.server.accept()
#         while self.status == 1:  # 循环收发数据包，长连接
#             # 接收客户端消息，
#             data = client.recv(self.BUF_SIZE)
#             text = data.decode()
#             # 如果接收到客户端消息就像客户端发送world
#             if text != "":
#                 print(text)  # python3 要使用decode
#                 client.send("world".encode())
#                 # client.close() #连接不断开，长连接
#
#
# if __name__ == "__main__":
#     server = Server("localhost", 8083)
#     server.createServer()
#     server.startServer()

# 模拟webcoket客户端发送消息
from websocket import create_connection
# from websocket import create_connection
# ws = create_connection("ws://localhost:8080/websocket")
# print ("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print ("Sent")
# print ("Reeiving...")
# result =  ws.recv()
# print ("Received '%s'" % result)
# ws.close()

# import websocket
# try:
#     import thread
# except ImportError:
#     import _thread as thread
# import time
#
# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     thread.start_new_thread(run, ())
#
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://localhost:8080/websocket",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()
