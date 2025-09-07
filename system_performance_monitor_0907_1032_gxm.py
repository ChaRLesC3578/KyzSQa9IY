# 代码生成时间: 2025-09-07 10:32:31
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QPushButton, QWidget, QVBoxLayout, QTextEdit
import psutil

# 系统性能监控工具
class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('System Performance Monitor')
        self.setGeometry(100, 100, 800, 600)
        
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建CPU使用率标签
        self.cpu_label = QLabel('CPU Usage: 0%')
        # 创建内存使用率标签
        self.mem_label = QLabel('Memory Usage: 0%')
        # 创建磁盘使用率标签
        self.disk_label = QLabel('Disk Usage: 0%')
        
        # 将标签添加到布局
        main_layout.addWidget(self.cpu_label)
        main_layout.addWidget(self.mem_label)
        main_layout.addWidget(self.disk_label)

        # 创建一个文本编辑框用于显示日志信息
        self.log_text_edit = QTextEdit()
        main_layout.addWidget(self.log_text_edit)

        # 创建一个按钮用于开始监控
        self.start_button = QPushButton('Start Monitoring')
        self.start_button.clicked.connect(self.startMonitoring)
        main_layout.addWidget(self.start_button)

        # 设置中央窗口部件
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def startMonitoring(self):
        # 启动监控线程
        self.monitor_thread = MonitoringThread()
        self.monitor_thread.update_signal.connect(self.updateMonitor)
        self.monitor_thread.log_signal.connect(self.logInfo)
        self.monitor_thread.start()

    def updateMonitor(self, cpu_usage, mem_usage, disk_usage):
        # 更新监控数据
        self.cpu_label.setText(f'CPU Usage: {cpu_usage}%')
        self.mem_label.setText(f'Memory Usage: {mem_usage}%')
        self.disk_label.setText(f'Disk Usage: {disk_usage}%')

    def logInfo(self, info):
        # 将日志信息添加到文本编辑框
        self.log_text_edit.append(info)

# 监控线程类
class MonitoringThread(QThread):
    update_signal = pyqtSignal(float, float, float)
    log_signal = pyqtSignal(str)
    
    def run(self):
        try:
            while True:
                # 获取系统性能数据
                cpu_usage = psutil.cpu_percent(interval=1)
                mem_usage = psutil.virtual_memory().percent
                disk_usage = psutil.disk_usage('/').percent
                
                # 发射信号更新监控数据
                self.update_signal.emit(cpu_usage, mem_usage, disk_usage)
                
                # 发射信号记录日志信息
                self.log_signal.emit(f'CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%, Disk Usage: {disk_usage}%')
                
                # 暂停一段时间再继续监控
                time.sleep(1)
        except Exception as e:
            self.log_signal.emit(f'Error occurred: {str(e)}')

# 主函数
def main():
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建系统性能监控工具实例
    monitor = SystemMonitor()
    monitor.show()
    
    # 运行应用程序
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()