# 代码生成时间: 2025-09-15 02:13:55
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np

"""
    Data Cleaning and Preprocessing Tool using Python and PyQt5.
    This tool provides a simple GUI for users to load, clean, and preprocess data.
"""

class DataCleaningTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Data Cleaning and Preprocessing Tool')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Add a label
        self.label = QLabel('Data Cleaning and Preprocessing Tool', central_widget)
        layout.addWidget(self.label)

        # Add a button to load data
        self.load_button = QPushButton('Load Data', central_widget)
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)

        # Add a table widget to display data
        self.table_widget = QTableWidget(central_widget)
        layout.addWidget(self.table_widget)

        # Set the central widget and layout
        self.setCentralWidget(central_widget)

    def load_data(self):
        # Open a file dialog to select a CSV file
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open CSV file', '.', 'CSV files (*.csv)', options=options)

        if filename:
            try:
                # Load the data into a pandas DataFrame
                data = pd.read_csv(filename)

                # Set the table widget with the loaded data
                row_count = data.shape[0]
                col_count = data.shape[1]
                self.table_widget.setRowCount(row_count)
                self.table_widget.setColumnCount(col_count)
                self.table_widget.setHorizontalHeaderLabels(data.columns)
                for i in range(row_count):
                    for j in range(col_count):
                        self.table_widget.setItem(i, j, QTableWidgetItem(str(data.iloc[i, j])))
            except pd.errors.EmptyDataError:
                print('The file is empty.')
            except pd.errors.ParserError:
                print('Error parsing the file.')
            except Exception as e:
                print(f'An error occurred: {e}')


def main():
    # Create a Qt application
    app = QApplication(sys.argv)

    # Create an instance of the DataCleaningTool class
    tool = DataCleaningTool()
    tool.show()

    # Start the Qt application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()