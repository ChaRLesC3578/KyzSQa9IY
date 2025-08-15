# 代码生成时间: 2025-08-16 00:39:40
import os
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
"""
批量文件重命名工具
使用PyQt框架创建一个图形界面，允许用户选择文件夹，输入文件名规则，
然后批量重命名文件夹中的文件。
"""

class BatchFileRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '批量文件重命名工具'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签和输入框
        self.label = QLabel('文件夹路径:', self)
        self.path_input = QLineEdit(self)
        self.label2 = QLabel('文件名规则:', self)
        self.name_input = QLineEdit(self)

        # 创建选择文件夹按钮
        self.btn_browse = QPushButton('浏览', self)
        self.btn_browse.clicked.connect(self.browse_folder)

        # 创建重命名按钮
        self.btn_rename = QPushButton('重命名', self)
        self.btn_rename.clicked.connect(self.rename_files)

        # 将控件添加到布局中
        layout.addWidget(self.label)
        layout.addWidget(self.path_input)
        layout.addWidget(self.btn_browse)
        layout.addWidget(self.label2)
        layout.addWidget(self.name_input)
        layout.addWidget(self.btn_rename)

        # 设置布局
        self.setLayout(layout)

    @pyqtSlot()
    def browse_folder(self):
        """
        浏览文件夹并设置文件夹路径
        """
        self.folder_path, _ = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if self.folder_path:
            self.path_input.setText(self.folder_path)

    @pyqtSlot()
    def rename_files(self):
        """
        根据文件名规则批量重命名文件夹中的文件
        """
        folder_path = self.path_input.text()
        name_pattern = self.name_input.text()
        if not folder_path or not name_pattern:
            print('请输入文件夹路径和文件名规则')
            return

        try:
            files = os.listdir(folder_path)
            for i, file in enumerate(files):
                if not re.match(r'[^/\
]+', file):  # 排除文件夹
                    continue
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, f'{re.sub(r'\W+', "", file)}_{i+1}_{name_pattern}')
                os.rename(old_path, new_path)
            print('文件重命名完成')
        except Exception as e:
            print(f'发生错误：{e}')

if __name__ == '__main__':
    app = QApplication([])
    ex = BatchFileRenamer()
    ex.show()
    app.exec_()