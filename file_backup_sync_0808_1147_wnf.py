# 代码生成时间: 2025-08-08 11:47:56
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

"""
File Backup and Sync Tool using Python and PyQt5.
This tool allows users to select a source directory and a destination directory.
It will then backup and sync files from the source to the destination.
"""

class FileBackupSync(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle('File Backup and Sync Tool')
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create source directory label and button
        self.source_label = QLabel('Source Directory: ')
        layout.addWidget(self.source_label)
        self.source_button = QPushButton('Select Source Directory')
        self.source_button.clicked.connect(self.select_source_directory)
        layout.addWidget(self.source_button)
        self.source_directory = ''

        # Create destination directory label and button
        self.dest_label = QLabel('Destination Directory: ')
        layout.addWidget(self.dest_label)
        self.dest_button = QPushButton('Select Destination Directory')
        self.dest_button.clicked.connect(self.select_destination_directory)
        layout.addWidget(self.dest_button)
        self.destination_directory = ''

        # Create backup and sync button
        self.backup_button = QPushButton('Backup and Sync')
        self.backup_button.clicked.connect(self.backup_and_sync)
        layout.addWidget(self.backup_button)

        # Set layout
        self.setLayout(layout)

    def select_source_directory(self):
        # Open file dialog to select source directory
        directory = QFileDialog.getExistingDirectory(self, 'Select Source Directory')
        if directory:
            self.source_directory = directory
            self.source_label.setText(f'Source Directory: {self.source_directory}')

    def select_destination_directory(self):
        # Open file dialog to select destination directory
        directory = QFileDialog.getExistingDirectory(self, 'Select Destination Directory')
        if directory:
            self.destination_directory = directory
            self.dest_label.setText(f'Destination Directory: {self.destination_directory}')

    def backup_and_sync(self):
        # Check if source and destination directories are selected
        if not self.source_directory or not self.destination_directory:
            QMessageBox.warning(self, 'Warning', 'Please select both source and destination directories.')
            return

        try:
            # Create destination directory if it does not exist
            if not os.path.exists(self.destination_directory):
                os.makedirs(self.destination_directory)

            # Iterate through files in source directory
            for filename in os.listdir(self.source_directory):
                file_path = os.path.join(self.source_directory, filename)
                dest_file_path = os.path.join(self.destination_directory, filename)

                # If file, copy file to destination directory
                if os.path.isfile(file_path):
                    shutil.copy2(file_path, dest_file_path)
                # If directory, recursively sync directory
                elif os.path.isdir(file_path):
                    shutil.copytree(file_path, dest_file_path, dirs_exist_ok=True)

            QMessageBox.information(self, 'Success', 'Backup and sync completed successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')

if __name__ == '__main__':
    app = QApplication([])
    tool = FileBackupSync()
    tool.show()
    app.exec_()