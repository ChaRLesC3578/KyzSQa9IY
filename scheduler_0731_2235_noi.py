# 代码生成时间: 2025-07-31 22:35:52
import sys
import threading
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QTimer

# 定时任务调度器类
# NOTE: 重要实现细节
class TaskScheduler(QObject):
# NOTE: 重要实现细节
    # 信号，用于在任务执行时发出
# 优化算法效率
    taskExecuted = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimeout)
        self.tasks = []
        self.isRunning = False

    def addTask(self, task, interval):
        """
        添加任务
        :param task: 任务函数
# FIXME: 处理边界情况
        :param interval: 执行间隔（毫秒）
        """
        self.tasks.append((task, interval))

    def start(self):
        """
        启动定时任务调度器
        """
        if not self.isRunning:
            self.timer.start(1000)  # 1秒检查一次任务队列
# FIXME: 处理边界情况
            self.isRunning = True

    def stop(self):
        "