# 代码生成时间: 2025-08-25 15:41:28
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt

"""
数据统计分析器
"""

class DataAnalysisTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '数据统计分析器'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        """初始化界面"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        self.open_file_button = QPushButton('打开文件', self)
        self.open_file_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_file_button)

        self.central_widget.setLayout(layout)

    def open_file(self):
        """打开文件对话框，选择数据文件"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择数据文件", "",
                                                  "CSV Files (*.csv);
Excel Files (*.xlsx)", options=options)
        if file_name:
            try:
                self.analyze_data(file_name)
            except Exception as e:
                print(f"Error analyzing data: {e}")

    def analyze_data(self, file_name):
        """分析数据"""
        try:
            # 根据文件类型读取数据
            if file_name.endswith('.csv'):
                data = pd.read_csv(file_name)
            elif file_name.endswith('.xlsx'):
                data = pd.read_excel(file_name)
            else:
                print("Unsupported file type")
                return

            # 展示数据概况
            print(data.describe())

            # 这里可以添加更多的数据分析功能
            # 例如：计算平均值、中位数、最大值等

        except Exception as e:
            print(f"Error reading file {file_name}: {e}")

    def run(self):
        """运行程序"""
        self.show()
        sys.exit(QApplication.instance().exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataAnalysisTool()
    ex.run()