# 代码生成时间: 2025-09-08 17:20:13
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QComboBox, QGridLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.figure as fig

"""
统计数据分析器
"""
class DataAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '统计数据分析器'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QGridLayout()
        self.main_widget.setLayout(layout)

        self.load_button = QPushButton('加载数据')
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button, 0, 0)

        self.analysis_type_combo = QComboBox()
        self.analysis_type_combo.addItems(['描述性统计', '相关性分析', '回归分析'])
        layout.addWidget(self.analysis_type_combo, 0, 1)

        self.run_button = QPushButton('运行分析')
        self.run_button.clicked.connect(self.run_analysis)
        layout.addWidget(self.run_button, 0, 2)

        self.result_label = QLabel('结果：')
        layout.addWidget(self.result_label, 1, 0, 1, 3)

    def load_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, '加载数据', '', 
                                                  'Excel Files (*.xls *.xlsx)', options=options)
        if file_name:
            try:
                self.data = pd.read_excel(file_name)
                self.result_label.setText('数据加载成功！')
            except Exception as e:
                QMessageBox.warning(self, '加载失败', f'加载数据失败：{e}')

    def run_analysis(self):
        analysis_type = self.analysis_type_combo.currentText()
        if analysis_type == '描述性统计':
            self.describe_statistics()
        elif analysis_type == '相关性分析':
            self.correlation_analysis()
        elif analysis_type == '回归分析':
            self.regression_analysis()

    def describe_statistics(self):
        if self.data is not None:
            desc_stats = self.data.describe()
            print(desc_stats)
            self.result_label.setText('描述性统计结果：' + str(desc_stats))
        else:
            QMessageBox.warning(self, '错误', '请先加载数据！')

    def correlation_analysis(self):
        if self.data is not None:
            corr_matrix = self.data.corr()
            print(corr_matrix)
            self.result_label.setText('相关性分析结果：' + str(corr_matrix))
        else:
            QMessageBox.warning(self, '错误', '请先加载数据！')

    def regression_analysis(self):
        if self.data is not None:
            X = self.data.iloc[:, :-1]
            y = self.data.iloc[:, -1]
            model = stats.linregress(X, y)
            print(model)
            self.result_label.setText('回归分析结果：' + str(model))
        else:
            QMessageBox.warning(self, '错误', '请先加载数据！')

    def show_plot(self, title, x, y):
        fig = fig.Figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        canvas = FigureCanvas(fig)
        self.main_widget.layout().addWidget(canvas)

    def show(self):
        super().show()

"""
运行程序
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataAnalysisApp()
    ex.show()
    sys.exit(app.exec_())