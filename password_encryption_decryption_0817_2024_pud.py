# 代码生成时间: 2025-08-17 20:24:56
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QErrorMessage
from PyQt5.QtCore import Qt

"""
一个简单的密码加密解密工具，使用PyQt5框架创建图形用户界面。
"""

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化界面元素
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Password Encryption/Decryption Tool')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 输入框
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Enter password')
        self.layout.addWidget(self.password_input)

        # 状态标签
        self.status_label = QLabel('')
        self.layout.addWidget(self.status_label)

        # 加密按钮
        password_encrypt_button = QPushButton('Encrypt')
        password_encrypt_button.clicked.connect(self.encrypt_password)
        self.layout.addWidget(password_encrypt_button)

        # 解密按钮
        password_decrypt_button = QPushButton('Decrypt')
        password_decrypt_button.clicked.connect(self.decrypt_password)
        self.layout.addWidget(password_decrypt_button)

    def encrypt_password(self):
        """
        对输入的密码进行加密。
        """
        input_password = self.password_input.text()
        if not input_password:
            self.status_label.setText('Please enter a password to encrypt.')
            return

        try:
            encrypted_password = hashlib.sha256(input_password.encode()).hexdigest()
            self.status_label.setText(f'Encrypted Password: {encrypted_password}')
        except Exception as e:
            self.status_label.setText(f'Error: {e}')

    def decrypt_password(self):
        """
        对加密的密码进行解密，当前实现为显示哈希值，真正的解密在SHA-256是不可逆的。
        """
        input_password = self.password_input.text()
        if not input_password:
            self.status_label.setText('Please enter a password to decrypt.')
            return

        try:
            # 由于SHA-256是不可逆的，这里只是显示输入的哈希值
            self.status_label.setText(f'Decrypted Password (SHA-256 Hash): {input_password}')
        except Exception as e:
            self.status_label.setText(f'Error: {e}')

    def run(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_manager = PasswordManager()
    password_manager.run()
    sys.exit(app.exec_())