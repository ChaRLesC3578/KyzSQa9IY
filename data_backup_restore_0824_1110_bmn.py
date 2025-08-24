# 代码生成时间: 2025-08-24 11:10:28
import os
import shutil
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QMessageBox

"""
A PyQt5 application for data backup and restore.
"""

class DataBackupRestore(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window's title and size
        self.setWindowTitle('Data Backup & Restore')
        self.setGeometry(100, 100, 300, 200)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add a label for instructions
        self.label = QLabel('Click the buttons below to backup or restore data.')
        layout.addWidget(self.label)

        # Add a button for backup
        self.backupButton = QPushButton('Backup Data')
        self.backupButton.clicked.connect(self.backupData)
        layout.addWidget(self.backupButton)

        # Add a button for restore
        self.restoreButton = QPushButton('Restore Data')
        self.restoreButton.clicked.connect(self.restoreData)
        layout.addWidget(self.restoreButton)

        # Set the layout for the window
        self.setLayout(layout)

    def backupData(self):
        try:
            # Get the source directory to backup
            source_dir = QFileDialog.getExistingDirectory(self, 'Select Source Directory')
            if not source_dir:
                return

            # Get the destination directory for backup
            dest_dir = QFileDialog.getSaveFileName(self, 'Select Backup Destination')[0]
            if not dest_dir:
                return

            # Create a timestamped backup directory
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_dir = os.path.join(dest_dir, f'backup_{timestamp}')
            os.makedirs(backup_dir, exist_ok=True)

            # Perform the backup
            shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)
            QMessageBox.information(self, 'Backup Success', 'Data has been successfully backed up.')
        except Exception as e:
            QMessageBox.critical(self, 'Backup Error', f'An error occurred: {e}')

    def restoreData(self):
        try:
            # Get the source directory for restore
            source_dir = QFileDialog.getExistingDirectory(self, 'Select Backup Source Directory')
            if not source_dir:
                return

            # Get the destination directory for restore
            dest_dir = QFileDialog.getExistingDirectory(self, 'Select Destination Directory')
            if not dest_dir:
                return

            # Perform the restore
            shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
            QMessageBox.information(self, 'Restore Success', 'Data has been successfully restored.')
        except Exception as e:
            QMessageBox.critical(self, 'Restore Error', f'An error occurred: {e}')

    def closeEvent(self, event):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication([])
    window = DataBackupRestore()
    window.show()
    app.exec_()