# 代码生成时间: 2025-09-15 14:58:19
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    """主窗口类，负责主题切换功能"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面"""
        self.setWindowTitle('主题切换器')
        self.setGeometry(100, 100, 300, 200)

        # 设置按钮和布局
        self.button = QPushButton('切换主题', self)
        self.button.clicked.connect(self.changeTheme)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def changeTheme(self):
        """更改应用程序的主题"""
        color, ok = QColorDialog.getColor()
        if ok:
            palette = self.palette()
            palette.setColor(QPalette.Window, color)
            self.setPalette(palette)
        else:
            print("主题切换已取消")

def main():
    """主函数，程序入口点"""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
