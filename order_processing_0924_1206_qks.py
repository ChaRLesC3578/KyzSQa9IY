# 代码生成时间: 2025-09-24 12:06:11
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

# 订单类
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = 'Pending'

    def confirm_order(self):
        """确认订单"""
        self.status = 'Confirmed'
        return f'Order {self.order_id} confirmed successfully.'

    def process_order(self):
        """处理订单"""
        if self.status != 'Confirmed':
            raise ValueError('Order must be confirmed before processing.')
        self.status = 'Processed'
        return f'Order {self.order_id} processed successfully.'

    def ship_order(self):
        """发货"""
        if self.status != 'Processed':
            raise ValueError('Order must be processed before shipping.')
        self.status = 'Shipped'
        return f'Order {self.order_id} shipped successfully.'

# 订单处理窗口类
class OrderProcessingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Order Processing System')
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        """初始化用户界面"""
        layout = QVBoxLayout()
        btn_confirm = QPushButton('Confirm Order')
        btn_process = QPushButton('Process Order')
        btn_ship = QPushButton('Ship Order')

        btn_confirm.clicked.connect(self.confirm_order)
        btn_process.clicked.connect(self.process_order)
        btn_ship.clicked.connect(self.ship_order)

        layout.addWidget(btn_confirm)
        layout.addWidget(btn_process)
        layout.addWidget(btn_ship)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.order = None

    def confirm_order(self):
        """用户点击确认订单"""
        if self.order is None:
            QMessageBox.warning(self, 'Error', 'No order to confirm.')
            return
        try:
            result = self.order.confirm_order()
            QMessageBox.information(self, 'Success', result)
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def process_order(self):
        """用户点击处理订单"""
        if self.order is None:
            QMessageBox.warning(self, 'Error', 'No order to process.')
            return
        try:
            result = self.order.process_order()
            QMessageBox.information(self, 'Success', result)
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def ship_order(self):
        """用户点击发货订单"""
        if self.order is None:
            QMessageBox.warning(self, 'Error', 'No order to ship.')
            return
        try:
            result = self.order.ship_order()
            QMessageBox.information(self, 'Success', result)
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))

    def create_order(self, order_id, customer_name):
        """创建新订单"""
        self.order = Order(order_id, customer_name)
        QMessageBox.information(self, 'Success', f'Order {order_id} created successfully.')

# 主函数
def main():
    app = QApplication(sys.argv)
    window = OrderProcessingWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()