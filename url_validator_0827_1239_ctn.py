# 代码生成时间: 2025-08-27 12:39:04
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QUrl

"""
A simple PyQt5 application to validate the validity of a URL link.
"""

class UrlValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout
        self.layout = QVBoxLayout()

        # Create a label for the URL input
        self.urlLabel = QLabel('Enter URL to validate: ', self)
        self.layout.addWidget(self.urlLabel)

        # Create a line edit for the user to enter the URL
        self.urlInput = QLineEdit(self)
        self.layout.addWidget(self.urlInput)

        # Create a button to trigger the validation
        self.validateButton = QPushButton('Validate', self)
        self.validateButton.clicked.connect(self.validateUrl)
        self.layout.addWidget(self.validateButton)

        # Set the layout for the main window
        self.setLayout(self.layout)
        self.setWindowTitle('URL Validator')
        self.setGeometry(300, 300, 300, 200)

    def validateUrl(self):
        # Retrieve the URL from the line edit
        url = self.urlInput.text()

        # Check if the URL is valid using QUrl
        is_valid = self.is_valid_url(url)

        # Show a message box with the result
        if is_valid:
            QMessageBox.information(self, 'Validation Result', 'The URL is valid.')
        else:
            QMessageBox.warning(self, 'Validation Result', 'The URL is invalid.')

    def is_valid_url(self, url):
        # Use QUrl to check if the URL is valid
        qurl = QUrl(url)
        return qurl.isValid() and qurl.scheme() != ''

def main():
    app = QApplication(sys.argv)
    ex = UrlValidator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
