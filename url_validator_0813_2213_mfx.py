# 代码生成时间: 2025-08-13 22:13:29
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

"""
URL Validator using Python and PyQt5.
This program is designed to check the validity of a given URL.
"""

class URLValidator(QWidget):
    """
    A class representing a PyQt5 GUI for URL validation.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the UI components."""
        self.title = 'URL Validator'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initWindow()

    def initWindow(self):
        """Set up the main window."""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QVBoxLayout()

        # URL input field
        self.urlInput = QLineEdit(self)
        self.urlInput.setPlaceholderText('Enter URL here')
        layout.addWidget(self.urlInput)

        # Validate button
        validateButton = QPushButton('Validate', self)
        validateButton.clicked.connect(self.validateURL)
        layout.addWidget(validateButton)

        # Status label
        self.statusLabel = QLabel(self)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)
        self.show()

    def validateURL(self):
        """Validate the URL and update the status label."""
        url = self.urlInput.text()
        try:
            response = requests.head(url)
            if response.status_code == 200:
                self.statusLabel.setText('URL is valid!')
            else:
                self.statusLabel.setText('URL is invalid or not reachable.')
        except requests.RequestException as e:
            self.statusLabel.setText(f'An error occurred: {e}')

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = URLValidator()
    sys.exit(app.exec_())