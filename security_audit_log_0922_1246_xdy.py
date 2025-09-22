# 代码生成时间: 2025-09-22 12:46:20
import logging
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import datetime

# 设置日志文件
LOG_FILE = 'security_audit.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityAuditLog(QMainWindow):
    """安全审计日志窗口类"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面"""
        self.setWindowTitle('安全审计日志')
        self.setGeometry(100, 100, 800, 600)

        # 创建文本框用于显示日志
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setStyleSheet('background-color: #f0f0f0;')

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        # 创建中心窗口部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 显示日志文件内容
        self.showLogs()

    def showLogs(self):
        """显示日志文件内容"""
        try:
            with open(LOG_FILE, 'r') as file:
                logs = file.read()
                self.textEdit.setText(logs)
        except FileNotFoundError:
            logging.error('日志文件未找到')
            self.textEdit.setText('日志文件未找到')
        except Exception as e:
            logging.error(f'显示日志时发生错误: {e}')
            self.textEdit.setText('显示日志时发生错误')

    def logEvent(self, event_message):
        """记录事件到日志"""
        logging.info(event_message)
        self.showLogs()

# 运行程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = SecurityAuditLog()
    main_window.show()
    sys.exit(app.exec_())