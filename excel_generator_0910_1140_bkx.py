# 代码生成时间: 2025-09-10 11:40:04
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
from openpyxl import Workbook

class ExcelGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('Excel Table Generator')
        self.setGeometry(100, 100, 600, 400)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个按钮，点击后打开文件对话框
        self.open_button = QPushButton('Open Excel File')
        self.open_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.open_button)

        # 创建一个按钮，点击后生成Excel表格
        self.generate_button = QPushButton('Generate Excel File')
        self.generate_button.clicked.connect(self.generate_excel_file)
        layout.addWidget(self.generate_button)

        # 创建一个容器Widget，添加布局
        self.container = QWidget()
        self.container.setLayout(layout)

        # 设置容器Widget为中央Widget
        self.setCentralWidget(self.container)

    def open_file_dialog(self):
        # 打开文件对话框，选择Excel文件
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)", options=options)
        if fileName:
            self.filename = fileName

    def generate_excel_file(self):
        # 生成Excel文件
        if hasattr(self, 'filename'):
            try:
                wb = Workbook()
                wb.save(self.filename)
                print(f'Excel file generated successfully: {self.filename}')
            except Exception as e:
                print(f'Error generating Excel file: {e}')
        else:
            print('Please select an Excel file first.')

if __name__ == '__main__':
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建Excel表格自动生成器窗口实例
    excel_generator = ExcelGenerator()

    # 显示窗口
    excel_generator.show()

    # 运行应用程序
    sys.exit(app.exec_())