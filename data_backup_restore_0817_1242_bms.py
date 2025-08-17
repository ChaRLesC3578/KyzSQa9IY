# 代码生成时间: 2025-08-17 12:42:25
import sys
import os
import shutil
import zipfile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

"""
A PyQt5 application for data backup and restore.
"""

class DataBackupRestoreApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create backup button
        self.backup_button = QPushButton('Backup Data')
        self.backup_button.clicked.connect(self.backup_data)
        layout.addWidget(self.backup_button)

        # Create restore button
        self.restore_button = QPushButton('Restore Data')
        self.restore_button.clicked.connect(self.restore_data)
        layout.addWidget(self.restore_button)

        # Set layout to the widget
        self.setLayout(layout)
        self.setWindowTitle('Data Backup & Restore')
        self.resize(300, 100)

    def backup_data(self):
        try:
            # Get backup directory
            directory = QFileDialog.getExistingDirectory(self, 'Select Backup Directory')
            if not directory:
                raise ValueError('No directory selected')
            # Define source and destination
            source = '/path/to/your/data/folder'
            destination = os.path.join(directory, 'backup.zip')
            # Zip and copy files
            with zipfile.ZipFile(destination, 'w') as zipf:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        zipf.write(os.path.join(root, file),
                                   os.path.relpath(os.path.join(root, file), source))
            QMessageBox.information(self, 'Backup Successful', 'Data backup completed successfully')
        except Exception as e:
            QMessageBox.critical(self, 'Backup Failed', str(e))

    def restore_data(self):
        try:
            # Get restore directory
            directory = QFileDialog.getExistingDirectory(self, 'Select Restore Directory')
            if not directory:
                raise ValueError('No directory selected')
            # Define source and destination
            source = QFileDialog.getOpenFileName(self, 'Select Backup File',
                                             directory, 'Backup Files (*.zip)')[0]
            if not source:
                raise ValueError('No file selected')
            destination = '/path/to/your/data/folder'
            # Unzip and copy files
            with zipfile.ZipFile(source, 'r') as zipf:
                zipf.extractall(destination)
            QMessageBox.information(self, 'Restore Successful', 'Data restore completed successfully')
        except Exception as e:
            QMessageBox.critical(self, 'Restore Failed', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataBackupRestoreApp()
    window.show()
    sys.exit(app.exec_())