# 代码生成时间: 2025-09-11 04:57:59
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLineEdit, QMessageBox

"""
A simple configuration manager application using PyQt.
This application allows users to create, read, update, and delete configuration files.
"""

class ConfigManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Config Manager')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText('Enter config file path')
        self.layout.addWidget(self.file_path_input)

        self.config_text_edit = QTextEdit()
        self.layout.addWidget(self.config_text_edit)

        self.load_button = QPushButton('Load')
        self.load_button.clicked.connect(self.loadConfig)
        self.layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.saveConfig)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def loadConfig(self):
        """Load configuration file content into text edit."""
        file_path = self.file_path_input.text()
        if not file_path:
            QMessageBox.warning(self, 'Warning', 'Please enter a file path.')
            return

        if not os.path.exists(file_path):
            QMessageBox.warning(self, 'Warning', 'File does not exist.')
            return

        try:
            with open(file_path, 'r') as file:
                config_data = json.load(file)
                self.config_text_edit.setText(json.dumps(config_data, indent=4))
        except json.JSONDecodeError:
            QMessageBox.critical(self, 'Error', 'Invalid JSON format.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def saveConfig(self):
        """Save configuration content from text edit to file."""
        file_path = self.file_path_input.text()
        if not file_path:
            QMessageBox.warning(self, 'Warning', 'Please enter a file path.')
            return

        try:
            config_data = json.loads(self.config_text_edit.toPlainText())
            with open(file_path, 'w') as file:
                json.dump(config_data, file, indent=4)
            QMessageBox.information(self, 'Success', 'Config saved successfully.')
        except json.JSONDecodeError:
            QMessageBox.critical(self, 'Error', 'Invalid JSON format.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

if __name__ == '__main__':
    app = QApplication([])
    manager = ConfigManager()
    manager.show()
    app.exec_()