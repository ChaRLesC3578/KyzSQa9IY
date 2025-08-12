# 代码生成时间: 2025-08-13 00:05:47
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QPalette, QStyle


class MainWindow(QMainWindow):
    """ 主窗口类，实现主题切换功能 """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ 初始化用户界面 """
        self.setWindowTitle('Theme Switcher')
        self.setGeometry(100, 100, 300, 200)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个按钮，用于切换主题
        self.button = QPushButton('Switch Theme', self)
        self.button.clicked.connect(self.switchTheme)

        # 将按钮添加到布局中
        layout.addWidget(self.button)

        # 创建一个widget作为中心widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def switchTheme(self):
        """ 切换主题的方法 """
        palette = self.palette()
        if palette.color(QPalette.Window).name() == '#ffffff':
            # 设置主题为深色模式
            palette.setColor(QPalette.Window, QColor(33, 33, 33))
            palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
            palette.setColor(QPalette.Base, QColor(33, 33, 33))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.Text, QColor(220, 220, 220))
            palette.setColor(QPalette.Button, QColor(33, 33, 33))
            palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
            palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, QColor(180, 180, 180))
        else:
            # 设置主题为浅色模式
            palette.setColor(QPalette.Window, QColor(255, 255, 255))
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
            palette.setColor(QPalette.Base, QColor(255, 255, 255))
            palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            palette.setColor(QPalette.Text, QColor(0, 0, 0))
            palette.setColor(QPalette.Button, QColor(255, 255, 255))
            palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
            palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
            palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

        self.setPalette(palette)


if __name__ == '__main__':
    # 创建一个应用实例
    app = QApplication(sys.argv)

    # 创建主窗口实例
    mainWin = MainWindow()
    mainWin.show()

    # 运行应用，返回退出码
    sys.exit(app.exec_())