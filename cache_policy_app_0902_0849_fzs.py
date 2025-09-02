# 代码生成时间: 2025-09-02 08:49:16
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer

# 缓存策略类
class CachePolicy:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        """获取缓存数据，如果缓存失效则返回None"""
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def set(self, key, value, ttl=3600):
        """设置缓存数据，包含过期时间ttl（秒）"""
        self.cache[key] = (value, ttl)

    def check_cache(self):
        """检查缓存并删除过期的数据"""
        current_time = self.current_time()
        for key, (value, ttl) in list(self.cache.items()):
            if current_time - ttl > self.cache[key][1]:
                del self.cache[key]

    @staticmethod
    def current_time():
        """获取当前时间戳（秒）"""
        from time import time
        return int(time())

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cache_policy = CachePolicy()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Cache Policy App')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.cache_label = QLabel('Cache:', self)
        layout.addWidget(self.cache_label)

        self.set_button = QPushButton('Set Cache', self)
        self.set_button.clicked.connect(self.set_cache)
        layout.addWidget(self.set_button)

        self.get_button = QPushButton('Get Cache', self)
        self.get_button.clicked.connect(self.get_cache)
        layout.addWidget(self.get_button)

        self.clear_button = QPushButton('Clear Cache', self)
        self.clear_button.clicked.connect(self.clear_cache)
        layout.addWidget(self.clear_button)

        self.result_label = QLabel('', self)
        layout.addWidget(self.result_label)

    def set_cache(self):
        key = 'test_key'
        value = 'test_value'
        self.cache_policy.set(key, value)
        self.result_label.setText(f'Set cache: {key} = {value}')

    def get_cache(self):
        key = 'test_key'
        data = self.cache_policy.get(key)
        if data is not None:
            self.result_label.setText(f'Get cache: {key} = {data}')
        else:
            self.result_label.setText(f'Cache expired or not found for key: {key}')

    def clear_cache(self):
        self.cache_policy.cache.clear()
        self.result_label.setText('Cache cleared')

    def check_cache_timer(self):
        """定时检查缓存并删除过期数据"""
        self.cache_policy.check_cache()

# 应用类
class CachePolicyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = MainWindow()
        self.main_window.show()
        self.timer = QTimer(self.main_window.check_cache_timer, 300000)  # 5分钟检查一次缓存
        self.timer.start()
        self.exec_()

if __name__ == '__main__':
    app = CachePolicyApp(sys.argv)
