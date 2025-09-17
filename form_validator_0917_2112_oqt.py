# 代码生成时间: 2025-09-17 21:12:08
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

"""
A simple PyQt5 form validator application.
This application creates a form with a single input field,
and a submit button. It validates the input when the button is clicked.
"""

class FormValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        # Create layout and widgets
        self.layout = QVBoxLayout()
        self.input_label = QLabel("Enter your name: ", self)
        self.input_field = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.validate_input)

        # Add widgets to layout
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.submit_button)

        # Set the layout for the main window
        self.setLayout(self.layout)
        self.setWindowTitle('Form Validator')
        self.setGeometry(300, 300, 200, 100)

    def validate_input(self):
        """Validate the input from the user."""
        # Get the input text
        input_text = self.input_field.text()

        # Check if the input is not empty
        if input_text.strip():
            QMessageBox.information(self, "Success", "Input is valid!")
        else:
            QMessageBox.warning(self, "Error", "Input cannot be empty.")

# Check if the script is run directly
if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create the form validator window
    validator = FormValidator()

    # Show the window
    validator.show()

    # Execute the application's main loop
    sys.exit(app.exec_())