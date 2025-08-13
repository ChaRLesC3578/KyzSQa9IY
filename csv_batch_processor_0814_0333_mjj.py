# 代码生成时间: 2025-08-14 03:33:58
import csv
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class CSVBatchProcessor(QWidget):
    """
    A PyQt5 GUI application for processing multiple CSV files.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface.
        """
        self.setWindowTitle('CSV Batch Processor')
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        self.label = QLabel('Select CSV files to process', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.openButton = QPushButton('Open Files', self)
        self.openButton.clicked.connect(self.openFiles)
        layout.addWidget(self.openButton)

        self.setLayout(layout)

    def openFiles(self):
        """
        Opens a file dialog for selecting CSV files and processes them.
        """
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Open Files", "", "CSV Files (*.csv)", options=options)
        if files:
            self.processFiles(files)
        else:
            print('No files selected.')

    def processFiles(self, files):
        """
        Processes the selected CSV files.
        """
        for file in files:
            try:
                with open(file, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    headers = next(reader)  # Assume the first row is the header
                    for row in reader:
                        # Process each row here
                        print(f'Processing row: {row}')
            except Exception as e:
                print(f'Error processing file {file}: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    processor = CSVBatchProcessor()
    processor.show()
    sys.exit(app.exec_())