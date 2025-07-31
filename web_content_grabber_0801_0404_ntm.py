# 代码生成时间: 2025-08-01 04:04:26
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QDesktopServices

"""
Web Content Grabber is a PyQt application that allows users to enter a URL,
and then it retrieves the content of the webpage.
"""

class WebContentGrabber(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Web Content Grabber')
        self.setGeometry(300, 300, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # URL input
        self.url_label = QLabel('Enter URL:', self)
        layout.addWidget(self.url_label)
        self.url_input = QTextEdit(self)
        self.url_input.setPlaceholderText('http://example.com')
        layout.addWidget(self.url_input)

        # Fetch button
        self.fetch_button = QPushButton('Fetch Content', self)
        self.fetch_button.clicked.connect(self.fetch_content)
        layout.addWidget(self.fetch_button)

        # Content display
        self.content_label = QLabel('Webpage Content:', self)
        layout.addWidget(self.content_label)
        self.content_display = QTextEdit(self)
        self.content_display.setReadOnly(True)
        layout.addWidget(self.content_display)

        # Error label
        self.error_label = QLabel('', self)
        self.error_label.setStyleSheet('QLabel { color: red; }')
        layout.addWidget(self.error_label)

        self.setLayout(layout)

    def fetch_content(self):
        # Clear previous content
        self.content_display.clear()
        self.error_label.clear()

        # Get the URL from the input field
        url = self.url_input.toPlainText()

        try:
            response = requests.get(url)
            response.raise_for_status()
            # Parse the content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Get the text from the parsed content
            content = soup.get_text()
            self.content_display.setText(content)
        except requests.exceptions.RequestException as e:
            error_message = f'Failed to retrieve content: {e}'
            self.error_label.setText(error_message)
        except Exception as e:
            error_message = f'An unexpected error occurred: {e}'
            self.error_label.setText(error_message)

    def run(self):
        self.show()
        sys.exit(QApplication.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebContentGrabber()
    ex.run()
