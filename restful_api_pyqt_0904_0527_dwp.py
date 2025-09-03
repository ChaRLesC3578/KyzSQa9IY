# 代码生成时间: 2025-09-04 05:27:39
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QGuiApplication

# RESTful API 客户端类
class RestfulApiClient:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.request_finished)

    def get(self, endpoint):
        # 发起 GET 请求
        url = QUrl(self.api_base_url + endpoint)
        request = QNetworkRequest(url)
        self.manager.get(request)

    def post(self, endpoint, data):
        # 发起 POST 请求
        url = QUrl(self.api_base_url + endpoint)
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, 'application/json')
        self.manager.post(request, data)

    def request_finished(self, reply):
        # 处理请求完成
        if reply.error() == QNetworkReply.NoError:
            print('Response received: ' + reply.readAll().data().decode('utf-8'))
        else:
            print('Error: ' + reply.errorString())
        reply.deleteLater()

# PyQt 窗体类
class RestfulApiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口
        self.setWindowTitle('RESTful API Client')
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        # 设置按钮和文本框
        self.get_button = QPushButton('Get Request')
        self.get_button.clicked.connect(self.send_get_request)
        layout.addWidget(self.get_button)

        self.post_button = QPushButton('Post Request')
        self.post_button.clicked.connect(self.send_post_request)
        layout.addWidget(self.post_button)

        self.text_area = QTextEdit()
        layout.addWidget(self.text_area)

        self.setLayout(layout)

    def send_get_request(self):
        # 发送 GET 请求
        self.client.get('/api/data')

    def send_post_request(self):
        # 发送 POST 请求
        self.client.post('/api/data', b'{"key": "value"}')

# 主程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RestfulApiApp()
    ex.client = RestfulApiClient('https://api.example.com')
    ex.show()
    sys.exit(app.exec_())
