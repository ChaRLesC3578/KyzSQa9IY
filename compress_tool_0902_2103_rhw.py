# 代码生成时间: 2025-09-02 21:03:09
import sys
import zipfile
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout,
                             QMessageBox, QLabel, QProgressBar)

"""
Compress Tool is a PyQt application to compress and decompress files.
It demonstrates the use of PyQt for file operations and GUI interactions.
"""

class CompressTool(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Compress Tool')
        self.setGeometry(100, 100, 300, 200)

        self.compressButton = QPushButton('Compress Files', self)
        self.compressButton.clicked.connect(self.compressFiles)
        self.compressButton.resize(200, 50)
        self.compressButton.move(50, 50)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.compressButton)
        self.setLayout(self.layout)

    def compressFiles(self):
        try:
            # Get the file paths from the user
            fileName, _ = QFileDialog.getOpenFileNames(self, 'Select Files to Compress',
                                                       '', 'All Files (*)')
            if fileName:
                # Get the destination path for the compressed file
                destination, _ = QFileDialog.getSaveFileName(self, 'Save Compressed File',
                                                          'compressed.zip', 'ZIP Files (*.zip)')
                if destination:
                    # Compress the files
                    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        for file in fileName:
                            zipf.write(file, os.path.basename(file))
                    QMessageBox.information(self, 'Success', 'Files compressed successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

# Create the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CompressTool()
    ex.show()
    sys.exit(app.exec_())