# 代码生成时间: 2025-09-09 01:12:50
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSlot

# 购物车类
class ShoppingCart:
    def __init__(self):
        self.items = []

    # 添加商品到购物车
    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart.")

    # 移除购物车中的商品
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            print(f"{item} not found in the cart.")

    # 显示购物车中的商品
    def display_items(self):
        for item in self.items:
            print(f"{item}")

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self, shopping_cart):
        super().__init__()
        self.cart = shopping_cart
        self.init_ui()

    # 初始化用户界面
    def init_ui(self):
        self.setWindowTitle("Shopping Cart")
        self.setGeometry(100, 100, 800, 600)
        self.set_up_widgets()

    # 设置用户界面部件
    def set_up_widgets(self):
        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        self.item_label = QLabel("Enter item name to add to cart: ")
        layout.addWidget(self.item_label)

        self.item_input = QLineEdit()
        layout.addWidget(self.item_input)

        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item_to_cart)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Item\)
        self.remove_button.clicked.connect(self.remove_item_from_cart)
        layout.addWidget(self.remove_button)

        self.display_button = QPushButton("Display Cart\)
        self.display_button.clicked.connect(self.display_cart_items)
        layout.addWidget(self.display_button)

        self.item_list = QTextEdit()
        layout.addWidget(self.item_list)

    # 添加商品到购物车
    @pyqtSlot()
    def add_item_to_cart(self):
        item = self.item_input.text()
        if item:
            self.cart.add_item(item)
            self.item_input.clear()
        else:
            print("Item name cannot be empty.")

    # 从购物车移除商品
    @pyqtSlot()
    def remove_item_from_cart(self):
        item = self.item_input.text()
        if item:
            self.cart.remove_item(item)
            self.item_input.clear()
        else:
            print("Item name cannot be empty.")

    # 显示购物车中的商品
    @pyqtSlot()
    def display_cart_items(self):
        self.item_list.clear()
        self.cart.display_items()
        for item in self.cart.items:
            self.item_list.append(f"{item}\
")

# 主函数
def main():
    app = QApplication(sys.argv)
    cart = ShoppingCart()
    window = MainWindow(cart)
    window.show()
    sys.exit(app.exec_())

# 程序入口点
if __name__ == "__main__":
    main()