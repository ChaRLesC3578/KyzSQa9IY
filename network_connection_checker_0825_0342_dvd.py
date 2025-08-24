# 代码生成时间: 2025-08-25 03:42:26
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QNetworkAccessManager, QNetworkRequest
import requests


class NetworkConnectionChecker(QMainWindow):
    """
    A PyQt5 GUI application to check network connection status.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components.
        """
        self.setWindowTitle('Network Connection Checker')
        self.setGeometry(100, 100, 400, 300)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create text edit widget to display the status
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        # Create and add check button
        self.check_button = QPushButton('Check Connection')
        self.check_button.clicked.connect(self.check_connection)
        layout.addWidget(self.check_button)

    def check_connection(self):
        """
        Check the network connection status and display the result in the text edit widget.
        """
        try:
            # Use requests library to check connection
            response = requests.get('https://www.google.com', timeout=5)
            if response.status_code == 200:
                self.text_edit.setText('Connected to the internet.')
            else:
                self.text_edit.setText('Failed to connect to the internet. Status code: ' + str(response.status_code))
        except requests.ConnectionError:
            self.text_edit.setText('No network connection detected.')
        except requests.Timeout:
            self.text_edit.setText('Connection timed out.')
        except Exception as e:
            self.text_edit.setText('An error occurred: ' + str(e))
        finally:
            self.text_edit.ensureCursorVisible()


def main():
    """
    Create the application and run it.
    """
    app = QApplication(sys.argv)
    window = NetworkConnectionChecker()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
