# 代码生成时间: 2025-08-26 06:42:24
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import requests
from bs4 import BeautifulSoup

class WebContentGrabber(QMainWindow):
    """A PyQt5 application to grab content from a webpage."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Web Content Grabber')
        self.setGeometry(100, 100, 600, 400)

        # Create the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a label to display instructions
        self.label = QLabel('Enter URL to grab content:', self)
        layout.addWidget(self.label)

        # Create a text edit to input the URL
        self.url_input = QTextEdit(self)
        layout.addWidget(self.url_input)

        # Create a button to trigger the content grab
        self.grab_button = QPushButton('Grab Content', self)
        self.grab_button.clicked.connect(self.grab_content)
        layout.addWidget(self.grab_button)

        # Create a text area to display the fetched content
        self.content_display = QTextEdit(self)
        self.content_display.setReadOnly(True)
        layout.addWidget(self.content_display)

    def grab_content(self):
        # Read the URL from the text input
        url = self.url_input.toPlainText()
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            # Handle any request errors
            self.content_display.setText(f'Error: {e}')
            return
        try:
            # Parse the content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the body content
            content = soup.body.prettify()
        except Exception as e:
            # Handle any parsing errors
            self.content_display.setText(f'Error parsing content: {e}')
            return
        # Display the content in the text area
        self.content_display.setText(content)

def main():
    app = QApplication(sys.argv)
    main_window = WebContentGrabber()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()