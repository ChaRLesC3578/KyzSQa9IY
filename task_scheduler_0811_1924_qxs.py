# 代码生成时间: 2025-08-11 19:24:40
import sys
from PyQt5.QtCore import QCoreApplication, QTimer, QMetaObject, Q_ARG
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import datetime
import threading

"""
定时任务调度器
"""
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.run_tasks)

    def add_task(self, task, interval):
        """添加任务到调度器"""
        self.tasks.append((task, interval))
        self.start_timer()

    def start_timer(self):
        """启动定时器"""
        if not self.timer.isActive():
            self.timer.start(1000)

    def run_tasks(self):
        """运行所有任务"""
        for task, _ in self.tasks:
            try:
                task()
            except Exception as e:
                print(f"任务执行出错: {e}")

"""
主程序
"""
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('定时任务调度器')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.add_task_btn = QPushButton('添加任务')
        self.add_task_btn.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_btn)

        self.status_label = QLabel('状态：就绪')
        layout.addWidget(self.status_label)

    def add_task(self):
        def sample_task():
            self.status_label.setText(f'状态：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} 任务执行')

        scheduler.add_task(sample_task, 5000)
        self.status_label.setText('状态：任务已添加')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    scheduler = TaskScheduler()
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())