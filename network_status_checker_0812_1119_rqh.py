# 代码生成时间: 2025-08-12 11:19:15
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QUrl, QNetworkRequest, QNetworkReply
from PyQt5.QtNetwork import QNetworkAccessManager

"""
Network Status Checker using PyQt framework.
This program checks the network connectivity and displays the result.
"""

class NetworkStatusChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main layout
        layout = QVBoxLayout(self)

        # Create a label to display the network status
        self.statusLabel = QLabel('Checking network status...', self)
        layout.addWidget(self.statusLabel)

        # Create a button to trigger the network status check
        self.checkButton = QPushButton('Check Network Status', self)
        self.checkButton.clicked.connect(self.checkNetworkStatus)
        layout.addWidget(self.checkButton)

        # Set the window title and geometry
        self.setWindowTitle('Network Status Checker')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def checkNetworkStatus(self):
        """
        Check the network status by attempting to access a known URL.
        If the request fails, it indicates a network connectivity issue.
        """
        # Create a network access manager
        self.manager = QNetworkAccessManager()
        
        # Define the URL to check (using a public, reliable endpoint)
        url = QUrl('http://www.google.com')
        request = QNetworkRequest(url)

        # Send the request and handle the response
        reply = self.manager.get(request)
        reply.finished.connect(self.handleNetworkCheck)

    def handleNetworkCheck(self):
        """
        Handle the network check response and update the UI accordingly.
        """
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            self.statusLabel.setText('Network is connected!')
        else:
            self.statusLabel.setText('Network is disconnected!')
        reply.deleteLater()

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = NetworkStatusChecker()

    # Start the application event loop
    sys.exit(app.exec_())