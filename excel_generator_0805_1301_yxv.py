# 代码生成时间: 2025-08-05 13:01:10
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from openpyxl import Workbook
from openpyxl.styles import PatternFill


class ExcelGenerator(QWidget):
    """
    Excel表格自动生成器，使用PyQt5 GUI创建界面，并生成Excel文件。
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化用户界面。
        """
        self.setWindowTitle('Excel表格自动生成器')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)  # 设置行为5行
        self.tableWidget.setColumnCount(3)  # 设置列为3列

        # 设置表格标题行
        headers = ['列1', '列2', '列3']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # 填充单元格内容
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row, column, QTableWidgetItem(f'单元格 {row+1}-{column+1}'))

        layout.addWidget(self.tableWidget)

        # 添加按钮，点击后保存Excel文件
        self.saveButton = QPushButton('保存Excel', self)
        self.saveButton.clicked.connect(self.saveExcel)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)

    def saveExcel(self):
        """
        保存Excel文件。
        """
        # 打开文件保存对话框
        filename, _ = QFileDialog.getSaveFileName(self, '保存Excel文件', '/', 'Excel 文件 (*.xlsx)')

        if filename:
            try:
                # 创建一个新的工作簿
                wb = Workbook()
                ws = wb.active

                # 设置表格标题行
                headers = ['列1', '列2', '列3']
                ws.append(headers)

                # 将QTableWidget中的数据写入Excel
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        # 如果单元格为空，则写入空字符串
                        else:
                            row_data.append('')
                    ws.append(row_data)

                # 保存工作簿到文件
                wb.save(filename)
                print(f'Excel文件已保存到：{filename}')
            except Exception as e:
                print(f'保存Excel文件时发生错误：{e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExcelGenerator()
    ex.show()
    sys.exit(app.exec_())