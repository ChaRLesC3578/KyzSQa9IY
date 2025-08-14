# 代码生成时间: 2025-08-14 13:49:26
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import requests

"""
网络连接状态检查器
使用Python和PyQt框架创建一个GUI程序，用于检查网络连接状态。
"""

class NetworkCheckThread(QThread):
    """
    线程类，用于在后台检查网络连接状态。
    """
    finished = pyqtSignal(bool)  # 发送一个布尔信号，指示连接状态
    def __init__(self):
        super().__init__()

    def run(self):
        """
        在线程中运行此方法，以检查网络连接状态。
        """
        try:
            # 尝试发送一个请求到一个可靠的外部服务器
            response = requests.get('https://www.google.com')
            # 如果请求成功，发送一个True信号
            if response.status_code == 200:
                self.finished.emit(True)
            else:
                self.finished.emit(False)
        except requests.ConnectionError:
            # 如果发生连接错误，发送一个False信号
            self.finished.emit(False)
        except Exception as e:
            # 其他异常处理
            print(f"An error occurred: {e}")
            self.finished.emit(False)

class MainWindow(QMainWindow):
    """
    GUI的主窗口类。
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化用户界面。
        """
        self.setWindowTitle('Network Connection Checker')
        self.setGeometry(100, 100, 200, 100)
        self.statusLabel = QLabel('Checking connection...', self)
        self.statusLabel.move(50, 40)
        self.show()

        # 创建一个线程实例
        self.thread = NetworkCheckThread()
        # 连接信号到槽函数
        self.thread.finished.connect(self.updateStatus)
        # 启动线程
        self.thread.start()

    def updateStatus(self, isConnected):
        """
        根据网络连接状态更新GUI。
        """
        if isConnected:
            self.statusLabel.setText('Connected to the internet.')
            self.statusLabel.setStyleSheet('QLabel { color: green; }')
        else:
            self.statusLabel.setText('No internet connection.')
            self.statusLabel.setStyleSheet('QLabel { color: red; }')

# 程序的入口点
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())