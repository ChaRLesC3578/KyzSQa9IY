# 代码生成时间: 2025-09-05 20:27:40
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QSpinBox, QComboBox
from PIL import Image

# 图片尺寸批量调整器应用
class BatchImageResizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始位置
        self.setWindowTitle('Batch Image Resizer')
        self.setGeometry(100, 100, 300, 150)

        # 创建垂直布局
        layout = QVBoxLayout()
# 优化算法效率

        # 添加选择文件夹按钮
        self.btn_select_folder = QPushButton('Select Folder')
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)
# TODO: 优化性能

        # 添加输入框显示选择的文件夹路径
        self.lbl_folder_path = QLabel('Selected Folder: None')
# FIXME: 处理边界情况
        layout.addWidget(self.lbl_folder_path)

        # 添加尺寸调整选项
        self.lbl_resize_option = QLabel('Resize Option:')
# 优化算法效率
        layout.addWidget(self.lbl_resize_option)
        self.cmb_resize_option = QComboBox()
        self.cmb_resize_option.addItems(['Width', 'Height', 'Both'])
        layout.addWidget(self.cmb_resize_option)

        # 添加新尺寸输入框
        self.lbl_new_size = QLabel('New Size:')
        layout.addWidget(self.lbl_new_size)
        self.spin_new_size = QSpinBox()
        self.spin_new_size.setRange(10, 10000)
        layout.addWidget(self.spin_new_size)

        # 添加调整按钮
# 扩展功能模块
        self.btn_resize = QPushButton('Resize Images')
        self.btn_resize.clicked.connect(self.resize_images)
        layout.addWidget(self.btn_resize)

        # 设置布局
        self.setLayout(layout)
# TODO: 优化性能

    def select_folder(self):
        # 选择文件夹
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.lbl_folder_path.setText(f'Selected Folder: {folder_path}')
            self.folder_path = folder_path

    def resize_images(self):
        # 检查是否选择了文件夹
        if not self.folder_path:
# FIXME: 处理边界情况
            print('Please select a folder first.')
            return

        # 检查新尺寸是否已输入
        if self.spin_new_size.value() <= 0:
# NOTE: 重要实现细节
            print('Please enter a valid new size.')
            return

        # 获取调整选项
        resize_option = self.cmb_resize_option.currentText()
        new_size = self.spin_new_size.value()

        # 遍历文件夹中的所有图片
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                try:
                    img_path = os.path.join(self.folder_path, filename)
                    img = Image.open(img_path)
# 改进用户体验

                    # 根据调整选项调整图片尺寸
# TODO: 优化性能
                    if resize_option == 'Width':
                        img = img.resize((new_size, img.height), Image.ANTIALIAS)
                    elif resize_option == 'Height':
# TODO: 优化性能
                        img = img.resize((img.width, new_size), Image.ANTIALIAS)
                    else:
                        img = img.resize((new_size, new_size), Image.ANTIALIAS)

                    # 保存调整后的图片
                    img.save(img_path)
                    print(f'Resized {filename}')
                except Exception as e:
                    print(f'Error resizing {filename}: {e}')
# 优化算法效率

    def main(self):
        # 运行应用
        BatchImageResizer()
        sys.exit(QApplication.instance().exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    BatchImageResizer().main()