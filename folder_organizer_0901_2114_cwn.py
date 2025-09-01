# 代码生成时间: 2025-09-01 21:14:13
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import Qt

"""
Folder Organizer GUI Application
This application allows users to select a folder and automatically organize its contents
into subfolders based on file extensions.
"""

class FolderOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Folder Organizer"
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create layout and widgets
        self.layout = QVBoxLayout()
        self.browse_button = QPushButton('Select Folder', self)
        self.browse_button.clicked.connect(self.browse_folder)
        self.folder_label = QLabel('Select a folder', self)
        self.layout.addWidget(self.browse_button)
        self.layout.addWidget(self.folder_label)
        self.setLayout(self.layout)

    def browse_folder(self):
        # Open file dialog to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.folder_label.setText(folder_path)
            self.organize_folder(folder_path)

    def organize_folder(self, folder_path):
        # Check if the folder path is valid
        if not os.path.exists(folder_path):
            raise ValueError("The folder path does not exist.")
        # Organize files into subfolders
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension:
                    new_folder_path = os.path.join(folder_path, file_extension[1:])
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)
                    new_file_path = os.path.join(new_folder_path, file)
                    shutil.move(file_path, new_file_path)

if __name__ == '__main__':
    app = QApplication([])
    ex = FolderOrganizer()
    ex.show()
    app.exec_()