# 代码生成时间: 2025-10-06 19:48:41
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog
from PyQt5.QtCore import pyqtSlot
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 数据加密传输工具
class DataEncryptionTool(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
# 添加错误处理

    def init_ui(self):
        # 设置窗口基本属性
        self.setWindowTitle('数据加密传输工具')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签
        self.label = QLabel('请输入需要加密或解密的文本：')
# TODO: 优化性能
        layout.addWidget(self.label)

        # 创建文本编辑框
# 优化算法效率
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # 创建按钮
# 扩展功能模块
        self.encrypt_button = QPushButton('加密')
        self.decrypt_button = QPushButton('解密')
        self.encrypt_button.clicked.connect(self.encrypt_data)
        self.decrypt_button.clicked.connect(self.decrypt_data)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)

        # 设置中央组件
        self.setLayout(layout)

    # 加密数据
    def encrypt_data(self):
        try:
            # 获取需要加密的文本
            text = self.text_edit.toPlainText()
            if not text:
                raise ValueError('文本为空')

            # 使用AES加密
# 改进用户体验
            cipher = AES.new(self.key, AES.MODE_ECB)
            ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
            ct_base64 = base64.b64encode(ct_bytes).decode('utf-8')

            # 显示加密结果
            self.text_edit.setText(ct_base64)
        except Exception as e:
            print(f'加密失败：{e}')

    # 解密数据
    def decrypt_data(self):
        try:
            # 获取需要解密的文本
# 改进用户体验
            ct_base64 = self.text_edit.toPlainText()
            if not ct_base64:
                raise ValueError('文本为空')

            # 解码base64
            ct_bytes = base64.b64decode(ct_base64)

            # 使用AES解密
            cipher = AES.new(self.key, AES.MODE_ECB)
            pt = unpad(cipher.decrypt(ct_bytes), AES.block_size).decode('utf-8')

            # 显示解密结果
            self.text_edit.setText(pt)
        except Exception as e:
            print(f'解密失败：{e}')

    # 设置密钥
    def set_key(self, key):
        self.key = key

# 主函数
def main():
    if len(sys.argv) != 2:
        print('请提供密钥参数')
        sys.exit(1)

    app = QApplication(sys.argv)
    key = sys.argv[1].encode('utf-8')  # 将命令行参数作为密钥
    tool = DataEncryptionTool()
    tool.set_key(key)
    tool.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
# FIXME: 处理边界情况