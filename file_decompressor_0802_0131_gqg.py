# 代码生成时间: 2025-08-02 01:31:00
import sys
import zipfile
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtCore import Qt


class FileDecompressor(QWidget):
    """
    A PyQt5 GUI application that decompresses zip files.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('File Decompressor')
        self.setGeometry(100, 100, 600, 400)

        # Layout for the buttons and label
        layout = QVBoxLayout()

        # Label to display instructions
        self.label = QLabel('Click the button to choose a zip file to decompress.')
        layout.addWidget(self.label)

        # Button to open file dialog to select a zip file
        self.btn_select_file = QPushButton('Select Zip File')
        self.btn_select_file.clicked.connect(self.selectFile)
        layout.addWidget(self.btn_select_file)

        # Button to start decompression
        self.btn_decompress = QPushButton('Decompress')
        self.btn_decompress.clicked.connect(self.decompressFile)
        self.btn_decompress.setEnabled(False)
        layout.addWidget(self.btn_decompress)

        # Progress bar to show the progress of decompression
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # Set the layout to the main window
        self.setLayout(layout)

    def selectFile(self):
        # Open file dialog to select a zip file
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open Zip File", "", "Zip Files (*.zip)", options=options)
        if self.fileName:
            self.btn_decompress.setEnabled(True)
            self.label.setText(f'Selected file: {os.path.basename(self.fileName)}')

    def decompressFile(self):
        # Decompress the selected zip file
        self.progress_bar.setValue(0)
        try:
            with zipfile.ZipFile(self.fileName, 'r') as zip_ref:
                # Get the total number of files to decompress
                total_files = len(zip_ref.infolist())
                # Create a directory to extract the files
                extract_to = os.path.join(os.path.dirname(self.fileName), 'extracted')
                os.makedirs(extract_to, exist_ok=True)
                for file_info in zip_ref.infolist():
                    # Extract each file
                    zip_ref.extract(file_info, extract_to)
                    # Update progress bar
                    self.progress_bar.setValue((self.progress_bar.value() + 1) % 100)
                self.label.setText('Decompression completed successfully.')
        except zipfile.BadZipFile:
            self.label.setText('Error: Selected file is not a valid zip file.')
        except Exception as e:
            self.label.setText(f'Error: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDecompressor()
    ex.show()
    sys.exit(app.exec_())