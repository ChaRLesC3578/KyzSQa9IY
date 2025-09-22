# 代码生成时间: 2025-09-23 00:55:34
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox

"""
A simple configuration file manager using PyQt.
"""

class ConfigManager(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Config Manager'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建布局
        layout = QVBoxLayout()

        # 创建文本编辑框，用于显示和编辑配置文件
        self.text_editor = QTextEdit()
        self.text_editor.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.text_editor)

        # 创建按钮，用于加载和保存配置文件
        self.load_button = QPushButton('Load Config')
        self.load_button.clicked.connect(self.load_config)
        layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save Config')
        self.save_button.clicked.connect(self.save_config)
        layout.addWidget(self.save_button)

        # 设置窗口的主布局
        self.setLayout(layout)

    def load_config(self):
        try:
            # 打开文件对话框，选择配置文件
            file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '/', 'Config Files (*.json)')
            if file_name:
                with open(file_name, 'r') as file:
                    # 读取配置文件内容
                    content = file.read()
                    self.text_editor.setText(content)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load config: {str(e)}')

    def save_config(self):
        try:
            # 打开文件对话框，保存配置文件
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '/', 'Config Files (*.json)')
            if file_name:
                # 写入配置文件内容
                with open(file_name, 'w') as file:
                    file.write(self.text_editor.toPlainText())
                QMessageBox.information(self, 'Success', 'Config saved successfully')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save config: {str(e)}')

    def closeEvent(self, event):
        # 确认是否保存配置文件
        ret = QMessageBox.question(self, 'Close', 'Do you want to save changes before closing?',
                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.save_config()
        elif ret == QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()

if __name__ == '__main__':
    app = QApplication([])
    ex = ConfigManager()
    ex.show()
    app.exec_()