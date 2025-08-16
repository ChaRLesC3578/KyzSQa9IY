# 代码生成时间: 2025-08-16 13:40:13
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

"""
A simple Python program that generates random numbers using the PyQt framework.
"""

class RandomNumberGenerator(QWidget):
    """Main application window."""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Random Number Generator')
        self.setGeometry(200, 200, 350, 150)

        layout = QVBoxLayout()

        # Input field for the user to enter the range of random numbers
        self.input_label = QLabel('Enter range (e.g., 1-100): ')
        self.input_field = QLineEdit()

        # Layout for the input field
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_field)

        # Button to generate a random number
        self.generate_button = QPushButton('Generate')
        self.generate_button.clicked.connect(self.generate_random_number)

        # Layout for the button
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)

        # Label to display the generated random number
        self.result_label = QLabel('Result: ')

        # Adding layouts to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def generate_random_number(self):
        """Generate a random number based on user input."""
        try:
            # Split the input range and convert to integers
            range_input = self.input_field.text().split('-')
            start = int(range_input[0])
            end = int(range_input[1])

            # Generate a random number within the specified range
            random_number = random.randint(start, end)
            self.result_label.setText(f'Result: {random_number}')
        except (ValueError, IndexError):
            # Handle errors in input format or range
            self.result_label.setText('Invalid input. Please enter a valid range (e.g., 1-100).')

def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    rng = RandomNumberGenerator()
    rng.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()