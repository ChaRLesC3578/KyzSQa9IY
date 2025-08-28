# 代码生成时间: 2025-08-28 22:16:57
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QSpinBox

"""
随机数生成器GUI程序
"""

class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        self.setWindowTitle('随机数生成器')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('随机数：', self)
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.updateRange)
        layout.addWidget(self.slider)

        self.spinBox = QSpinBox(self)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(10)
        self.spinBox.valueChanged.connect(self.updateRange)
        layout.addWidget(self.spinBox)

        self.button = QPushButton('生成随机数', self)
        self.button.clicked.connect(self.generateRandomNumber)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def updateRange(self):
        """更新随机数范围"""
        self.range = (self.slider.value(), self.spinBox.value())
        self.label.setText(f'随机数：{self.range[0]}-{self.range[1]}')

    def generateRandomNumber(self):
        """生成随机数"""
        try:
            random_num = random.randint(*self.range)
            self.label.setText(f'生成的随机数：{random_num}')
        except Exception as e:
            self.label.setText('生成随机数失败：' + str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = RandomNumberGenerator()
    generator.show()
    sys.exit(app.exec_())