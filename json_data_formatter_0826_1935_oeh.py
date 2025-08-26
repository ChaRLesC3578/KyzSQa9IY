# 代码生成时间: 2025-08-26 19:35:51
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox

"""
JSON数据格式转换器

该程序使用PyQt框架创建一个图形界面，允许用户输入JSON数据，并将数据格式化为美化后的JSON字符串。
"""

class JsonFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle("JSON 数据格式转换器")

        # 创建布局
        layout = QVBoxLayout()

        # 创建输入文本框
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText('请输入JSON数据...')
        layout.addWidget(self.input_text)

        # 创建格式化按钮
        self.format_button = QPushButton("格式化", self)
        self.format_button.clicked.connect(self.format_json)
        layout.addWidget(self.format_button)

        # 创建输出文本框
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # 设置布局
        self.setLayout(layout)

    def format_json(self):
        # 获取输入文本
        input_json = self.input_text.toPlainText()

        try:
            # 尝试解析JSON数据
            data = json.loads(input_json)
            # 格式化JSON数据
            formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
            self.output_text.setText(formatted_json)
        except json.JSONDecodeError as e:
            # 错误处理
            QMessageBox.critical(self, "错误", f"无效的JSON格式: {e.msg}")


def main():
    # 创建应用程序实例
    app = QApplication([])
    # 创建窗口实例
    window = JsonFormatter()
    # 显示窗口
    window.show()
    # 运行应用程序
    app.exec_()

if __name__ == '__main__':
    main()