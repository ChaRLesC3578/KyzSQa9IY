# 代码生成时间: 2025-09-14 20:02:29
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel

"""
Math Calculator - A simple calculator application using PyQt5.
This application provides basic mathematical operations: addition, subtraction, multiplication, and division.
"""

class MathCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Math Calculator')
        self.setGeometry(100, 100, 300, 200)

        # Create the central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create input and output fields
        self.input_field = QLineEdit(self)
        self.output_field = QLineEdit(self)
        self.output_field.setReadOnly(True)

        # Create labels for input and output fields
        self.input_label = QLabel('Enter expression:', self)
        self.output_label = QLabel('Result:', self)

        # Create buttons for mathematical operations
        self.add_button = QPushButton('Add (+)', self)
        self.subtract_button = QPushButton('Subtract (-)', self)
        self.multiply_button = QPushButton('Multiply (*)', self)
        self.divide_button = QPushButton('Divide (/)', self)

        # Add widgets to the layout
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.subtract_button)
        self.layout.addWidget(self.multiply_button)
        self.layout.addWidget(self.divide_button)

        # Connect signals to slots
        self.add_button.clicked.connect(self.add)
        self.subtract_button.clicked.connect(self.subtract)
        self.multiply_button.clicked.connect(self.multiply)
        self.divide_button.clicked.connect(self.divide)

        # Set the focus to the input field
        self.input_field.setFocus()

    def add(self):
        self.calculate_operator('+')

    def subtract(self):
        self.calculate_operator('-')

    def multiply(self):
        self.calculate_operator('*')

    def divide(self):
        self.calculate_operator('/')

    def calculate_operator(self, operator):
        try:
            # Split the input field by the operator and calculate the result
            numbers = self.input_field.text().split(operator)
            if len(numbers) != 2:
                self.output_field.setText('Error: Invalid expression')
                return

            num1 = float(numbers[0].strip())
            num2 = float(numbers[1].strip())

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    self.output_field.setText('Error: Division by zero')
                    return
                result = num1 / num2

            self.output_field.setText(str(result))
        except ValueError:
            self.output_field.setText('Error: Invalid number')
        except Exception as e:
            self.output_field.setText(f'Error: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = MathCalculator()
    calculator.show()
    sys.exit(app.exec_())