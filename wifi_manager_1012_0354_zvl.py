# 代码生成时间: 2025-10-12 03:54:25
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QProcess, pyqtSlot

"""
WiFi Manager application using PyQt framework to manage WiFi networks.
This application allows users to scan for available WiFi networks,
connect to a selected network, and disconnect from the current network.
"""

class WifiManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title and size of the window
        self.setWindowTitle('WiFi Manager')
        self.setGeometry(100, 100, 400, 300)

        # Create layout and widgets
        layout = QVBoxLayout()
        self.layout = layout

        self.scanButton = QPushButton('Scan Networks')
        self.scanButton.clicked.connect(self.scanNetworks)
        layout.addWidget(self.scanButton)

        self.networkList = QTextEdit()
        self.networkList.setReadOnly(True)
        layout.addWidget(self.networkList)

        self.connectButton = QPushButton('Connect')
        self.connectButton.clicked.connect(self.connectToNetwork)
        layout.addWidget(self.connectButton)

        self.disconnectButton = QPushButton('Disconnect')
        self.disconnectButton.clicked.connect(self.disconnectFromNetwork)
        layout.addWidget(self.disconnectButton)

        self.setLayout(layout)

    def scanNetworks(self):
        """Scan for available WiFi networks."""
        try:
            output = subprocess.check_output(['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi'])
            networks = output.decode('utf-8').splitlines()
            self.networkList.setText('
'.join(networks))
        except subprocess.CalledProcessError as e:
            self.networkList.setText(f'Error scanning networks: {e}')

    def connectToNetwork(self):
        "