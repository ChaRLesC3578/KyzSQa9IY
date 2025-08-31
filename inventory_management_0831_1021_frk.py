# 代码生成时间: 2025-08-31 10:21:06
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt

# 库存管理系统主窗口类
class InventoryManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始位置及大小
        self.setWindowTitle('Inventory Management System')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局和控件
        self.centralWidget = QWidget(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        self.createWidgets()

    def createWidgets(self):
        # 添加产品名称输入框
        self.productNameLabel = QLabel('Product Name: ')
        self.layout.addWidget(self.productNameLabel)
        self.productNameLineEdit = QLineEdit()
        self.layout.addWidget(self.productNameLineEdit)

        # 添加库存数量输入框
        self.quantityLabel = QLabel('Quantity: ')
        self.layout.addWidget(self.quantityLabel)
        self.quantityLineEdit = QLineEdit()
        self.layout.addWidget(self.quantityLineEdit)

        # 添加增加库存按钮
        self.addInventoryButton = QPushButton('Add Inventory')
        self.addInventoryButton.clicked.connect(self.addInventory)
        self.layout.addWidget(self.addInventoryButton)

        # 添加显示库存按钮
        self.showInventoryButton = QPushButton('Show Inventory')
        self.showInventoryButton.clicked.connect(self.showInventory)
        self.layout.addWidget(self.showInventoryButton)

        # 添加库存数据存储
        self.inventory = {}

    def addInventory(self):
        # 获取产品名称和数量
        productName = self.productNameLineEdit.text().strip()
        quantity = self.quantityLineEdit.text().strip()

        # 检查输入有效性
        if productName == '' or quantity == '':
            QMessageBox.warning(self, 'Warning', 'Please enter both product name and quantity.')
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Please enter a valid quantity.')
            return

        # 添加库存
        if productName in self.inventory:
            QMessageBox.warning(self, 'Warning', 'Product already exists in inventory.')
        else:
            self.inventory[productName] = quantity
            QMessageBox.information(self, 'Information', 'Inventory added successfully.')

    def showInventory(self):
        # 显示库存信息
        inventoryInfo = ''
        for productName, quantity in self.inventory.items():
            inventoryInfo += f'{productName}: {quantity}
'
        QMessageBox.information(self, 'Inventory', inventoryInfo)

# 主函数
def main():
    app = QApplication(sys.argv)
    window = InventoryManagementSystem()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()