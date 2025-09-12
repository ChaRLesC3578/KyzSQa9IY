# 代码生成时间: 2025-09-12 23:14:04
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox

"""
API响应格式化工具
该程序使用PyQt框架创建一个简单的GUI，
允许用户输入API响应JSON字符串，
并提供一个按钮来格式化JSON输出。
"""

class ApiResponseFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('API Response Formatter')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel('Enter API Response JSON String:', self)
        layout.addWidget(self.label)

        # 创建文本编辑框
        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('Paste your JSON string here...')
        layout.addWidget(self.textEdit)

        # 创建格式化按钮
        self.formatButton = QPushButton('Format JSON', self)
        self.formatButton.clicked.connect(self.formatJson)
        layout.addWidget(self.formatButton)

        # 创建输出标签
        self.outputLabel = QLabel('Formatted JSON:', self)
        layout.addWidget(self.outputLabel)

        # 创建输出文本编辑框
        self.outputTextEdit = QTextEdit(self)
        self.outputTextEdit.setReadOnly(True)
        layout.addWidget(self.outputTextEdit)

        # 设置布局
        self.setLayout(layout)

    def formatJson(self):
        # 获取输入文本
        json_string = self.textEdit.toPlainText()

        try:
            # 尝试解析JSON
            json_data = json.loads(json_string)
            # 格式化JSON
            formatted_json = json.dumps(json_data, indent=4)
            # 显示格式化后的JSON
            self.outputTextEdit.setText(formatted_json)
        except json.JSONDecodeError as e:
            # 错误处理：如果JSON解析失败，显示错误消息
            QMessageBox.critical(self, 'Error', f'Invalid JSON: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ApiResponseFormatter()
    ex.show()
    sys.exit(app.exec_())