# 代码生成时间: 2025-08-02 15:51:53
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
哈希值计算工具
这个程序使用PyQt框架创建一个图形界面，用户可以输入字符串，
然后计算并显示其MD5、SHA-1和SHA-256哈希值。
# FIXME: 处理边界情况
"""

class HashCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
# 添加错误处理
        # 设置窗口标题和初始大小
        self.setWindowTitle("Hash Calculator")
        self.setGeometry(100, 100, 400, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 输入框
        self.inputText = QTextEdit(self)
# 增强安全性
        self.inputText.setPlaceholderText("Enter text here...")
        layout.addWidget(self.inputText)

        # 按钮
        self.calculateButton = QPushButton("Calculate", self)
# TODO: 优化性能
        self.calculateButton.clicked.connect(self.calculateHashes)
        layout.addWidget(self.calculateButton)

        # 输出框
        self.outputText = QTextEdit(self)
        self.outputText.setReadOnly(True)
        layout.addWidget(self.outputText)
# 改进用户体验

        # 布局设置
        self.setLayout(layout)

    def calculateHashes(self):
        """
        计算输入文本的哈希值并显示结果
        """
        input_text = self.inputText.toPlainText()
        if not input_text:
            self.outputText.setText("Please enter some text to hash.")
            return

        # 计算MD5哈希值
        md5_hash = hashlib.md5(input_text.encode()).hexdigest()

        # 计算SHA-1哈希值
        sha1_hash = hashlib.sha1(input_text.encode()).hexdigest()

        # 计算SHA-256哈希值
        sha256_hash = hashlib.sha256(input_text.encode()).hexdigest()

        # 显示结果
        result = f"MD5: {md5_hash}
# 增强安全性
SHA-1: {sha1_hash}
SHA-256: {sha256_hash}"
        self.outputText.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
# TODO: 优化性能
    calculator = HashCalculator()
    calculator.show()
    sys.exit(app.exec_())