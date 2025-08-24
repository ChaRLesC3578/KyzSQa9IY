# 代码生成时间: 2025-08-24 15:19:59
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

"""
库存管理系统
"""

class InventoryManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('库存管理系统')
        self.resize(800, 600)

        # 创建垂直布局
        layout = QVBoxLayout(self)

        # 创建添加按钮
        add_button = QPushButton('添加库存')
        add_button.clicked.connect(self.add_inventory)
        layout.addWidget(add_button)

        # 创建删除按钮
        delete_button = QPushButton('删除库存')
        delete_button.clicked.connect(self.delete_inventory)
        layout.addWidget(delete_button)

        # 创建表格显示库存信息
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['编号', '名称', '数量'])
        self.table.horizontalHeader().setSectionResizeMode(QTableWidget.QHeaderView.Stretch)
        layout.addWidget(self.table)

        # 设置窗口布局
        self.setLayout(layout)

    def add_inventory(self):
        # 获取输入的库存信息
        num = self.num_lineedit.text()
        name = self.name_lineedit.text()
        quantity = self.quantity_lineedit.text()

        # 验证输入是否有效
        if not num or not name or not quantity:
            QMessageBox.warning(self, '错误', '请填写所有字段')
            return

        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, '错误', '数量必须为整数')
            return

        # 添加库存信息到表格
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(num))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(quantity)))

    def delete_inventory(self):
        # 获取选中的行
        row = self.table.currentRow()

        # 验证是否选中行
        if row == -1:
            QMessageBox.warning(self, '错误', '请选中要删除的库存')
            return

        # 删除选中的行
        self.table.removeRow(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InventoryManagement()
    window.show()
    sys.exit(app.exec_())