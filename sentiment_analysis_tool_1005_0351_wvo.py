# 代码生成时间: 2025-10-05 03:51:21
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import Qt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# 确保已下载vader lexicon
nltk.download('vader_lexicon')

class SentimentAnalysisTool(QMainWindow):
    """情感分析工具主窗口"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        self.setWindowTitle('情感分析工具')
        self.setGeometry(100, 100, 600, 400)

        # 设置中心窗口
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 添加文本编辑框
        self.text_edit = QTextEdit(central_widget)
        self.text_edit.setPlaceholderText('请输入文本进行情感分析...')
        layout.addWidget(self.text_edit)

        # 添加分析按钮
        self.analyze_button = QPushButton('分析情感', central_widget)
        self.analyze_button.clicked.connect(self.analyze_sentiment)
        layout.addWidget(self.analyze_button)

        # 添加结果标签
        self.result_label = QLabel(central_widget)
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

    def analyze_sentiment(self):
        """分析文本情感"""
        text = self.text_edit.toPlainText()
        try:
            # 使用VADER进行情感分析
            sia = SentimentIntensityAnalyzer()
            sentiment = sia.polarity_scores(text)
            result_text = f'正面情感: {sentiment[