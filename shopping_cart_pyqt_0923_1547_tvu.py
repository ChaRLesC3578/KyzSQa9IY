# 代码生成时间: 2025-09-23 15:47:05
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt

"""
购物车功能实现
使用Python和PyQt5框架创建一个简单的购物车程序。
"""

class ShoppingCart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle('Shopping Cart')
        self.setGeometry(100, 100, 400, 200)

        # 创建布局
        self.layout = QVBoxLayout()

        # 创建文本框，用于输入商品名称
        self.item_name = QLineEdit(self)
        self.layout.addWidget(QLabel('Item Name:'))
        self.layout.addWidget(self.item_name)

        # 创建文本框，用于输入商品数量
        self.item_quantity = QLineEdit(self)
        self.layout.addWidget(QLabel('Quantity:'))
        self.layout.addWidget(self.item_quantity)

        # 创建添加按钮
        self.add_button = QPushButton('Add to Cart', self)
        self.add_button.clicked.connect(self.addToCart)
        self.layout.addWidget(self.add_button)

        # 创建显示购物车内容的标签
        self.cart_display = QLabel('Cart is empty')
        self.layout.addWidget(self.cart_display)

        # 设置布局
        self.setLayout(self.layout)

    def addToCart(self):
        # 获取商品名称和数量
        item_name = self.item_name.text()
        quantity = self.item_quantity.text()

        # 检查输入是否有效
        if not item_name.strip() or not quantity.strip():
            QMessageBox.warning(self, 'Warning', 'Please enter both item name and quantity.')
            return

        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Please enter a valid quantity.')
            return

        # 将商品添加到购物车
        self.updateCart(item_name, quantity)

    def updateCart(self, item_name, quantity):
        # 获取当前购物车内容
        cart_contents = self.cart_display.text()

        # 更新购物车内容
        new_content = f'{cart_contents}<br>{item_name} - {quantity}'
        self.cart_display.setText(new_content)

        # 清空输入框
        self.item_name.clear()
        self.item_quantity.clear()

class ShoppingCartApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.cart = ShoppingCart()
        self.cart.show()

if __name__ == '__main__':
    app = ShoppingCartApp(sys.argv)
    sys.exit(app.exec_())