# 代码生成时间: 2025-08-18 14:49:48
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
JSON数据格式转换器

该程序使用PyQt框架创建一个简单的GUI应用程序，
用于将用户输入的JSON字符串转换为格式化的JSON数据。
"""

class JsonDataConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和布局
        self.setWindowTitle('JSON Data Converter')
        self.layout = QVBoxLayout()

        # 输入框
        self.input_label = QLabel('Enter JSON String:')
        self.input_text_edit = QTextEdit()
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text_edit)

        # 转换按钮
        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_json)
        self.layout.addWidget(self.convert_button)

        # 输出框
        self.output_label = QLabel('Formatted JSON:')
        self.output_text_edit = QTextEdit()
        self.output_text_edit.setReadOnly(True)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text_edit)

        # 设置布局
        self.setLayout(self.layout)
        self.show()

    def convert_json(self):
        # 获取输入的JSON字符串
        input_json = self.input_text_edit.toPlainText()

        try:
            # 尝试解析JSON字符串
            data = json.loads(input_json)

            # 格式化JSON数据
            formatted_json = json.dumps(data, indent=4)

            # 显示格式化后的JSON数据
            self.output_text_edit.setText(formatted_json)

        except json.JSONDecodeError as e:
            # 错误处理
            self.output_text_edit.setText(f'Error: {e}')

def main():
    app = QApplication([])
    converter = JsonDataConverter()
    app.exec_()

if __name__ == '__main__':
    main()