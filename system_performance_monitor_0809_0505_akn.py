# 代码生成时间: 2025-08-09 05:05:07
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QTimer

"""
A PyQt5 application for monitoring system performance.
This script creates a simple GUI that displays CPU and memory usage.
"""

class SystemPerformanceMonitor(QMainWindow):
# 添加错误处理
    def __init__(self):
        super().__init__()
        self.title = "System Performance Monitor"
        self.left = 100
# TODO: 优化性能
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)

        self.cpu_label = QLabel('CPU Usage: 0%', self)
        self.mem_label = QLabel('Memory Usage: 0%', self)

        layout.addWidget(self.cpu_label)
# NOTE: 重要实现细节
        layout.addWidget(self.mem_label)
# FIXME: 处理边界情况

        update_button = QPushButton('Update', self)
        update_button.clicked.connect(self.update_system_info)
        layout.addWidget(update_button)

        self.timer = QTimer(self.update_system_info)
        self.timer.timeout.connect(self.update_system_info)
# 扩展功能模块
        self.timer.start(1000)  # Update every second

    def update_system_info(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
# TODO: 优化性能
            mem = psutil.virtual_memory()
            mem_usage = mem.percent

            self.cpu_label.setText(f'CPU Usage: {cpu_usage}%')
            self.mem_label.setText(f'Memory Usage: {mem_usage}%')
        except Exception as e:
            print(f"Error updating system info: {e}")

    def closeEvent(self, event):
        self.timer.stop()
# 增强安全性
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    ex = SystemPerformanceMonitor()
    ex.show()
    sys.exit(app.exec_())
# 添加错误处理

if __name__ == '__main__':
    main()