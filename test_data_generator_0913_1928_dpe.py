# 代码生成时间: 2025-09-13 19:28:57
import random
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

"""
这是一个使用Python和PyQt框架创建的测试数据生成器。
该程序允许用户输入测试数据的参数，然后生成随机的测试数据。
"""

class TestDataGeneratorWidget(QWidget):
    """
    主窗口类，用于显示GUI和处理用户交互。
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化UI组件。
        """
        self.setWindowTitle('测试数据生成器')
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.param_input = QTextEdit()
        self.param_input.setPlaceholderText('输入测试数据参数，JSON格式')
        layout.addWidget(self.param_input)

        self.generate_button = QPushButton('生成测试数据')
        self.generate_button.clicked.connect(self.generate_test_data)
        layout.addWidget(self.generate_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

    def generate_test_data(self):
        """
        根据用户输入的参数生成测试数据。
        """
        try:
            params = self.param_input.toPlainText()
            params = json.loads(params)
            test_data = self.create_test_data(params)
            self.result_text.setText(json.dumps(test_data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError as e:
            self.result_text.setText(f'参数错误：{e}')
        except Exception as e:
            self.result_text.setText(f'生成测试数据时出错：{e}')

    def create_test_data(self, params):
        """
        根据参数生成测试数据。
        """
        test_data = []
        for _ in range(params.get('count', 1)):
            data = {}
            for key, spec in params.get('data_spec', {}).items():
                if spec['type'] == 'int':
                    data[key] = random.randint(spec.get('min', 0), spec.get('max', 100))
                elif spec['type'] == 'float':
                    data[key] = round(random.uniform(spec.get('min', 0.0), spec.get('max', 100.0)), 2)
                elif spec['type'] == 'str':
                    data[key] = ''.join(random.choices(spec.get('choices', ['a', 'b', 'c', 'd', 'e']), k=spec.get('length', 5)))
                else:
                    raise ValueError(f'不支持的数据类型：{spec[