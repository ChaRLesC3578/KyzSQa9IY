# 代码生成时间: 2025-09-06 18:06:43
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QIODevice, QSaveFile
from datetime import datetime
import logging
import os

# 配置日志记录器
logging.basicConfig(level=logging.INFO, filename='audit.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class SecurityAuditLog(QMainWindow):
    """安全审计日志GUI应用程序"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和尺寸
        self.setWindowTitle('Security Audit Log')
        self.setGeometry(100, 100, 600, 400)

        # 创建日志文本框
        self.logText = QTextEdit(self)
        self.logText.setReadOnly(True)
        self.logText.setLineWrapMode(QTextEdit.NoWrap)

        # 创建保存日志按钮
        self.saveButton = QPushButton('Save Log', self)
        self.saveButton.clicked.connect(self.saveLogToFile)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.logText)
        layout.addWidget(self.saveButton)

        # 创建中心小部件并设置布局
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def logEvent(self, message):
        """记录事件到日志"""
        logging.info(message)
        # 将日志信息添加到文本框
        self.logText.append(message)

    def saveLogToFile(self):
        """保存日志到文件"""
        file_name, _ = QSaveFile.getSaveFileName(
            self, 'Save Log File',
            os.path.expanduser('~') + '/security_audit_log.txt',
            'Text Files (*.txt)'
        )
        if file_name:
            try:
                with file_name.open('w') as f:
                    f.write(self.logText.toPlainText())
                self.logEvent(f'Log saved to {file_name}')
            except Exception as e:
                self.logEvent(f'Failed to save log: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    audit_log = SecurityAuditLog()
    audit_log.show()
    sys.exit(app.exec_())