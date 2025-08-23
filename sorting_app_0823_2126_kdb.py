# 代码生成时间: 2025-08-23 21:26:28
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import pyqtSlot

class SortingApp(QWidget):
    """A PyQt5 application to demonstrate sorting algorithms."""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title of the application
        self.setWindowTitle('Sorting Algorithm App')

        # Create a vertical box layout
        layout = QVBoxLayout()

        # Create a label to display instructions
        self.label = QLabel('Enter numbers separated by spaces for sorting:', self)
        layout.addWidget(self.label)

        # Create a text edit to input numbers
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        # Create a button to trigger sorting
        self.sortButton = QPushButton('Sort', self)
        self.sortButton.clicked.connect(self.sortNumbers)
        layout.addWidget(self.sortButton)

        # Create a label to display the result
        self.resultLabel = QLabel('Sorted numbers will appear here.', self)
        layout.addWidget(self.resultLabel)

        # Set the layout for the application
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def sortNumbers(self):
        # Retrieve the text from the text edit and split it into a list of numbers
        input_text = self.textEdit.toPlainText()
        try:
            numbers = [int(num) for num in input_text.split()]
            sorted_numbers = self.bubbleSort(numbers)
            self.resultLabel.setText(' '.join(map(str, sorted_numbers)))
        except ValueError:
            self.resultLabel.setText('Please enter valid integers separated by spaces.')

    def bubbleSort(self, arr):
        """Sorts an array using the Bubble Sort algorithm."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

# Check if the script is run directly
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sorting_app = SortingApp()
    sys.exit(app.exec_())