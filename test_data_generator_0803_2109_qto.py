# 代码生成时间: 2025-08-03 21:09:57
import random
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog
from PyQt5.QtCore import Qt

class TestDataGenerator(QWidget):
    """
    测试数据生成器GUI应用
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化UI组件
        """
        self.setWindowTitle('测试数据生成器')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.input_label = QLabel('输入数据数量：')
        layout.addWidget(self.input_label)
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('请输入数据数量')
        layout.addWidget(self.input_field)

        self.output_label = QLabel('输出文件路径：')
        layout.addWidget(self.output_label)
        self.output_field = QLineEdit()
        self.output_field.setPlaceholderText('点击选择文件保存路径')
        layout.addWidget(self.output_field)

        self.browse_button = QPushButton('浏览')
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        self.generate_button = QPushButton('生成数据')
        self.generate_button.clicked.connect(self.generate_data)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def browse_file(self):
        """
        浏览文件保存路径
        """
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, '选择文件保存路径', '',
                                                  'JSON Files (*.json)', options=options)
        if filename:
            self.output_field.setText(filename)

    def generate_data(self):
        """
        生成测试数据
        """
        try:
            count = int(self.input_field.text())
            if count <= 0:
                raise ValueError('数据数量必须大于0')

            data = self.create_test_data(count)
            if not self.output_field.text():
                raise ValueError('请选择文件保存路径')

            with open(self.output_field.text(), 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            self.show_message('数据生成成功')
        except ValueError as e:
            self.show_message(str(e))

    def create_test_data(self, count):
        """
        生成测试数据
        """
        data = []
        for _ in range(count):
            data.append({
                'id': random.randint(1, 100),
                'name': f'用户{random.randint(1, 100)}',
                'age': random.randint(18, 60),
                'gender': random.choice(['男', '女'])
            })
        return data

    def show_message(self, message):
        """
        显示消息
        """
        QMessageBox.information(self, '提示', message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TestDataGenerator()
    main_window.show()
    sys.exit(app.exec_())