# 代码生成时间: 2025-10-13 18:55:48
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

"""
客户关系管理系统
"""

class CustomerManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('客户关系管理系统')
        self.setGeometry(100, 100, 400, 300)

        # 布局
        layout = QVBoxLayout()

        # 输入框
        self.nameLineEdit = QLineEdit(self)
        self.phoneLineEdit = QLineEdit(self)
        self.emailLineEdit = QLineEdit(self)

        # 按钮
        addButton = QPushButton('添加客户', self)
        addButton.clicked.connect(self.addCustomer)

        # 标签
        self.infoLabel = QLabel('客户信息', self)

        # 添加控件到布局
        layout.addWidget(self.nameLineEdit)
        layout.addWidget(self.phoneLineEdit)
        layout.addWidget(self.emailLineEdit)
        layout.addWidget(addButton)
        layout.addWidget(self.infoLabel)

        # 设置中心控件
        centerWidget = QWidget()
        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)

    def addCustomer(self):
        """添加客户信息到系统"""
        name = self.nameLineEdit.text()
        phone = self.phoneLineEdit.text()
        email = self.emailLineEdit.text()

        if not name or not phone or not email:
            QMessageBox.warning(self, '警告', '所有字段都是必填的')
            return

        # 这里可以添加将客户信息保存到数据库的代码
        # 例如：self.saveCustomerToDatabase(name, phone, email)

        self.infoLabel.setText(f'客户信息：{name}, {phone}, {email}')

    def saveCustomerToDatabase(self, name, phone, email):
        """将客户信息保存到数据库"""
        # 这里应该包含数据库操作代码，例如使用SQLAlchemy等ORM工具
        # 为了简单起见，这里只是打印信息
        print(f'保存客户信息：{name}, {phone}, {email}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomerManagement()
    ex.show()
    sys.exit(app.exec_())
