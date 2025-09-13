# 代码生成时间: 2025-09-13 08:37:27
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

"""
这是一个使用PyQt框架创建的数据模型应用。
它包含一个主窗口，显示一个表格，用于展示数据。
"""

class DataModelApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面。"""
        self.setWindowTitle('数据模型应用')
        self.setGeometry(100, 100, 800, 600)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.initTable()
        
    def initTable(self):
        """初始化表格，添加表头和模拟数据。"""
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '年龄', '职业'])
        
        # 添加模拟数据
        self.tableWidget.setRowCount(5)
        for i in range(5):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(f'姓名{i+1}'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(f'{20 + i}岁'))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(f'职业{i+1}'))

    def errorHandling(self, error_message):
        """错误处理函数。"""
        print(f'错误：{error_message}')

    def closeEvent(self, event):
        """关闭事件处理。"""
        reply = QMessageBox.question(self, '退出', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = DataModelApp()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f'程序运行时发生错误：{e}')
