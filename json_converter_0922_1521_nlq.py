# 代码生成时间: 2025-09-22 15:21:59
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import pyqtSlot

"""
JSON数据格式转换器
使用Python和PyQt框架创建图形用户界面，允许用户输入JSON数据，
并提供一个按钮将其转换为格式化的JSON字符串。
"""

class JsonConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle('JSON Converter')

        # 创建布局
        layout = QVBoxLayout()

        # 创建输入框
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText('Enter JSON data here...')
        layout.addWidget(self.input_text)

        # 创建输出框
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText('Formatted JSON will appear here...')
        layout.addWidget(self.output_text)

        # 创建按钮
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_json)
        layout.addWidget(self.convert_button)

        # 创建状态标签
        self.status_label = QLabel(self)
        layout.addWidget(self.status_label)

        # 设置布局
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def convert_json(self):
        # 从输入框获取JSON数据
        json_data = self.input_text.toPlainText()
        try:
            # 尝试将输入的字符串转换为JSON对象
            data = json.loads(json_data)
            # 尝试将JSON对象转换为格式化的JSON字符串
            formatted_json = json.dumps(data, indent=4)
            # 将格式化的JSON字符串输出到输出框
            self.output_text.setText(formatted_json)
            # 更新状态标签
            self.status_label.setText('Success')
        except json.JSONDecodeError as e:
            # 如果JSON解析失败，显示错误信息
            self.output_text.setText('')
            self.status_label.setText(f'Error: {str(e)}')

# 程序入口点
if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = JsonConverter()
    sys.exit(app.exec_())