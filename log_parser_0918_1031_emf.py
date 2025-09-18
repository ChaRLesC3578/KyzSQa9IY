# 代码生成时间: 2025-09-18 10:31:39
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import pyqtSlot

# 定义日志解析类
class LogParser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和布局
        self.setWindowTitle('Log Parser Tool')
        self.layout = QVBoxLayout()

        # 添加按钮和文本框
        self.openButton = QPushButton('Open Log File')
        self.openButton.clicked.connect(self.openLogFile)
        self.layout.addWidget(self.openButton)

        self.textEdit = QTextEdit()
        self.layout.addWidget(self.textEdit)

        # 布置布局
        self.setLayout(self.layout)
        self.resize(600, 400)

    # 打开日志文件槽函数
    @pyqtSlot()
    def openLogFile(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Log File', '',
                                                 'Log Files (*.log);;All Files (*)', options=options)
        if filename:
            try:
                with open(filename, 'r') as file:
                    log_content = file.read()
                    self.parseLog(log_content)
            except IOError as e:
                print(f'Error opening file: {e}')

    # 解析日志文件函数
    def parseLog(self, log_content):
        # 假设日志文件有特定格式，这里使用正则表达式进行解析
        # 请根据实际日志格式调整正则表达式
        pattern = re.compile(r'\[(.*?)\]\[(INFO|ERROR|WARNING)\]\[(.*?)\] - (.*)')
        for match in pattern.finditer(log_content):
            timestamp, level, _, message = match.groups()
            formatted_message = f'[{timestamp} {level}] {message}'
            self.textEdit.append(formatted_message)

# 运行PyQt应用程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    parser = LogParser()
    parser.show()
    sys.exit(app.exec_())