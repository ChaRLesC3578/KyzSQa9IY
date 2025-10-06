# 代码生成时间: 2025-10-07 02:22:28
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
import base64

class EncryptionDecryptionApp(QWidget):
    """
    密码加密解密工具
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('Password Encryption/Decryption Tool')
        self.setGeometry(100, 100, 400, 300)

        # 创建布局和控件
        self.layout = QVBoxLayout()
        self.textEditInput = QTextEdit()
        self.textEditInput.setPlaceholderText('Enter your text here')
        self.textEditOutput = QTextEdit()
        self.textEditOutput.setPlaceholderText('Encrypted/Decrypted text will appear here')
        self.buttonEncrypt = QPushButton('Encrypt')
        self.buttonDecrypt = QPushButton('Decrypt')
        self.labelError = QLabel('')
        self.labelError.setStyleSheet('color: red')

        # 添加控件到布局
        self.layout.addWidget(QLabel('Input Text:'))
        self.layout.addWidget(self.textEditInput)
        self.layout.addWidget(QLabel('Output Text:'))
        self.layout.addWidget(self.textEditOutput)
        self.layout.addWidget(self.buttonEncrypt)
        self.layout.addWidget(self.buttonDecrypt)
        self.layout.addWidget(self.labelError)

        # 设置布局
        self.setLayout(self.layout)

        # 连接信号和槽
        self.buttonEncrypt.clicked.connect(self.encrypt)
        self.buttonDecrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        """
        加密输入的文本
        """
        input_text = self.textEditInput.toPlainText()
        try:
            encrypted_text = self.encrypt_text(input_text)
            self.textEditOutput.setText(encrypted_text)
            self.labelError.setText('')
        except Exception as e:
            self.labelError.setText(f'Error: {str(e)}')

    def decrypt(self):
        """
        解密输入的文本
        """
        input_text = self.textEditInput.toPlainText()
        try:
            decrypted_text = self.decrypt_text(input_text)
            self.textEditOutput.setText(decrypted_text)
            self.labelError.setText('')
        except Exception as e:
            self.labelError.setText(f'Error: {str(e)}')

    def encrypt_text(self, text):
        """
        使用AES加密文本
        """
        key = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_ECB)
        padded_text = pad(text.encode(), AES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted_text).decode() + '|' + base64.b64encode(key).decode()

    def decrypt_text(self, text):
        """
        使用AES解密文本
        """
        try:
            encrypted_text, key = text.split('|')
            encrypted_text = base64.b64decode(encrypted_text)
            key = base64.b64decode(key)
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted_padded_text = cipher.decrypt(encrypted_text)
            return unpad(decrypted_padded_text, AES.block_size).decode()
        except ValueError:
            raise ValueError('Invalid encrypted text format')
        except Exception as e:
            raise Exception(f'Decryption error: {str(e)}')

    def run(self):
        """
        运行应用程序
        """
        self.show()
        sys.exit(QApplication.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncryptionDecryptionApp()
    ex.run()