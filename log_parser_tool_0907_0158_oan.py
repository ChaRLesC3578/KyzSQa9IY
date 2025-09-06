# 代码生成时间: 2025-09-07 01:58:05
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt

"""
日志文件解析工具
"""
class LogParserTool(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """初始化UI组件"""
        self.setWindowTitle('日志文件解析工具')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        
        self.open_button = QPushButton('打开日志文件')
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
        self.setLayout(layout)
    
    def open_file(self):
        """打开日志文件对话框"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, '打开日志文件', '', 
                                                  '日志文件 (*.log)', options=options)
        if file_name:
            self.parse_log(file_name)
    
    def parse_log(self, file_name):
        """解析日志文件"""
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                log_content = file.read()
                self.log_text.setText(log_content)
        except FileNotFoundError:
            print('日志文件未找到')
        except Exception as e:
            print(f'解析日志文件时发生错误：{e}')

"""
程序入口
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = LogParserTool()
    tool.show()
    sys.exit(app.exec_())