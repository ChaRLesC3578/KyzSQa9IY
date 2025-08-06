# 代码生成时间: 2025-08-06 09:15:05
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

"""
A simple PyQt application that generates random numbers.

This program creates a window with a button to generate a random number
and displays it in a label. It also includes options to specify the range of the random number.
"""

class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title of the window
        self.setWindowTitle('Random Number Generator')

        # Create layout
        layout = QVBoxLayout()

        # Create input fields for minimum and maximum values
        self.minInput = QLineEdit(self)
        self.minInput.setPlaceholderText('Enter minimum value')
        self.maxInput = QLineEdit(self)
        self.maxInput = QLineEdit(self)
        self.maxInput.setPlaceholderText('Enter maximum value')

        # Create a label to display the generated random number
        self.resultLabel = QLabel('Click Generate to display a random number', self)

        # Create a button to generate a random number
        self.generateButton = QPushButton('Generate', self)
        self.generateButton.clicked.connect(self.on_generate)

        # Add widgets to the layout
        layout.addWidget(self.minInput)
        layout.addWidget(self.maxInput)
        layout.addWidget(self.generateButton)
        layout.addWidget(self.resultLabel)

        # Set the layout for the main window
        self.setLayout(layout)

    def on_generate(self):
        # Try to get the minimum and maximum values from the input fields
        try:
            min_val = int(self.minInput.text())
            max_val = int(self.maxInput.text())

            # Check if the values are valid
            if min_val > max_val:
                raise ValueError('Minimum value cannot be greater than maximum value.')

            # Generate a random number within the specified range
            random_number = random.randint(min_val, max_val)
            self.resultLabel.setText(f'Random number: {random_number}')
        except ValueError as e:
            # Handle any errors that occur during the random number generation
            self.resultLabel.setText(f'Error: {str(e)}')
        except Exception as e:
            # Handle any unexpected errors
            self.resultLabel.setText(f'Unexpected error: {str(e)}')

def main():
    app = QApplication(sys.argv)
    ex = RandomNumberGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()