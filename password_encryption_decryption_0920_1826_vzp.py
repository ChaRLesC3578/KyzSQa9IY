# 代码生成时间: 2025-09-20 18:26:33
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSlot

"""
密码加密解密工具
"""

class PasswordEncryptionDecryption(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化界面布局
        """
        self.setWindowTitle('Password Encryption Decryption Tool')
        self.setGeometry(100, 100, 300, 200)

        # 垂直布局
        layout = QVBoxLayout()

        # 文本输入框
        self.input_line_edit = QLineEdit(self)
        self.input_line_edit.setPlaceholderText('Enter password')
        layout.addWidget(self.input_line_edit)

        # 文本显示框
        self.output_text_edit = QTextEdit(self)
        layout.addWidget(self.output_text_edit)

        # 按钮
        self.encrypt_button = QPushButton('Encrypt', self)
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    @pyqtSlot()
    def encrypt(self):
        """
        密码加密
        """
        password = self.input_line_edit.text()
        if password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.output_text_edit.setText(hashed_password)
        else:
            self.output_text_edit.setText('Password cannot be empty')

    @pyqtSlot()
    def decrypt(self):
        """
        密码解密
        """
        # 由于SHA-256是不可逆的，这里只是将输入的密码显示在输出框中
        password = self.input_line_edit.text()
        self.output_text_edit.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_tool = PasswordEncryptionDecryption()
    password_tool.show()
    sys.exit(app.exec_())
