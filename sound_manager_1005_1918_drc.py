# 代码生成时间: 2025-10-05 19:18:48
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

"""
音效管理器
使用PyQt5创建一个简单的音效管理器，允许用户加载、播放、暂停和停止音频文件。
"""

class SoundManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle('音效管理器')
        self.setGeometry(100, 100, 400, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 创建按钮
        self.load_button = QPushButton('加载音效', self)
        self.play_button = QPushButton('播放音效', self)
        self.pause_button = QPushButton('暂停音效', self)
        self.stop_button = QPushButton('停止音效', self)

        # 添加按钮到布局
        layout.addWidget(self.load_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)

        # 设置中央部件
        self.setLayout(layout)

        # 连接信号和槽
        self.load_button.clicked.connect(self.load_sound)
        self.play_button.clicked.connect(self.play_sound)
        self.pause_button.clicked.connect(self.pause_sound)
        self.stop_button.clicked.connect(self.stop_sound)

        # 初始化播放器和视频部件
        self.player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.layout().addWidget(self.video_widget)

    def load_sound(self):
        # 打开文件对话框选择音频文件
        file_path, _ = QFileDialog.getOpenFileName(self, '选择音效文件', '.', 'Audio Files (*.mp3 *.wav)')
        if file_path:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            QMessageBox.information(self, '加载音效', '音效加载成功')
        else:
            QMessageBox.warning(self, '加载音效', '未选择任何文件')

    def play_sound(self):
        # 播放音效
        if self.player.media().isNull():
            QMessageBox.warning(self, '播放音效', '没有加载任何音效')
            return
        self.player.play()
        QMessageBox.information(self, '播放音效', '正在播放音效')

    def pause_sound(self):
        # 暂停音效
        if not self.player.media().isNull() and self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            QMessageBox.information(self, '暂停音效', '音效已暂停')
        else:
            QMessageBox.warning(self, '暂停音效', '音效未播放或已暂停')

    def stop_sound(self):
        # 停止音效
        if not self.player.media().isNull() and self.player.state() != QMediaPlayer.StoppedState:
            self.player.stop()
            QMessageBox.information(self, '停止音效', '音效已停止')
        else:
            QMessageBox.warning(self, '停止音效', '音效未播放')

    def closeEvent(self, event):
        # 关闭窗口时停止播放音效
        self.player.stop()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = SoundManager()
    main_window.show()
    sys.exit(app.exec_())