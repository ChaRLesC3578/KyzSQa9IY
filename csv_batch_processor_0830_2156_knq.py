# 代码生成时间: 2025-08-30 21:56:43
import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

"""
CSV文件批量处理器

这个程序允许用户选择一个CSV文件，然后对文件中的数据进行处理。
"""

class CSVBatchProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('CSV文件批量处理器')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建选择文件的按钮
        self.openButton = QPushButton('打开CSV文件')
        self.openButton.clicked.connect(self.openCSVFile)
        layout.addWidget(self.openButton)

        # 创建显示文件内容的文本编辑框
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        # 设置窗口布局
        self.setLayout(layout)

    def openCSVFile(self):
        # 打开文件对话框，选择CSV文件
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "打开CSV文件", "", "CSV Files (*.csv)", options=options)
        if fileName:
            try:
                # 读取CSV文件内容
                with open(fileName, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = [row for row in reader]

                # 显示CSV文件内容
                self.textEdit.setText('
'.join([','.join(row) for row in data]))
            except Exception as e:
                # 显示错误信息
                self.textEdit.setText(f'读取文件失败: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CSVBatchProcessor()
    ex.show()
    sys.exit(app.exec_())