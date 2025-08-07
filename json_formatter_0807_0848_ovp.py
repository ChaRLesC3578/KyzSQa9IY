# 代码生成时间: 2025-08-07 08:48:05
import sys
import json
# 扩展功能模块
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMessageBox
# NOTE: 重要实现细节
from PyQt5.QtCore import Qt

"""
A PyQt5 application to format JSON data.
This application allows users to input JSON data and format it into a more readable form.
"""

class JsonFormatter(QWidget):
    """
    The main widget of the PyQt5 application.
    It provides a GUI for users to input and format JSON data.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('JSON Formatter')
        self.setGeometry(100, 100, 600, 400)
# 添加错误处理

        self.json_input = QTextEdit()
# 扩展功能模块
        self.json_output = QTextEdit()
# NOTE: 重要实现细节
        self.json_output.setReadOnly(True)

        layout = QVBoxLayout()
        button = QPushButton('Format JSON', self)
# 优化算法效率
        button.clicked.connect(self.format_json)
        layout.addWidget(self.json_input)
        layout.addWidget(button)
        layout.addWidget(self.json_output)

        self.setLayout(layout)

    def format_json(self):
        """Format the input JSON data."""
        try:
# 改进用户体验
            json_data = self.json_input.toPlainText()
            # Attempt to parse the JSON data
            parsed_data = json.loads(json_data)
            # Format the JSON data
            formatted_data = json.dumps(parsed_data, indent=4)
            self.json_output.setText(formatted_data)
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            QMessageBox.critical(self, 'Error', f'Invalid JSON: {e}')
        except Exception as e:
            # Handle any other unexpected errors
            QMessageBox.critical(self, 'Error', f'An unexpected error occurred: {e}')

if __name__ == '__main__':
# NOTE: 重要实现细节
    app = QApplication(sys.argv)
    formatter = JsonFormatter()
    formatter.show()
    sys.exit(app.exec_())