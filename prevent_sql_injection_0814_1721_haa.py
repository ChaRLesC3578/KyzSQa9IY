# 代码生成时间: 2025-08-14 17:21:04
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton
from PyQt5.QtCore import Qt
import sqlite3

"""
A PyQt5 application that demonstrates how to prevent SQL injection by using parameterized queries.
"""

class SQLInjectionPrevention(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QFormLayout()

        # Create input fields
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Add input fields to layout
        layout.addRow('Username:', self.username_input)
        layout.addRow('Password:', self.password_input)

        # Create login button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        # Set layout for the main window
        self.setLayout(layout)
        self.setWindowTitle('SQL Injection Prevention')
        self.setGeometry(300, 300, 300, 150)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            # Prepare the SQL query with parameterized inputs
            query = "SELECT * FROM users WHERE username=? AND password=?"
            cursor.execute(query, (username, password))

            # Fetch the result
            if cursor.fetchone():
                print('Login successful')
            else:
                print('Login failed')

            # Close the database connection
            conn.close()
        except sqlite3.Error as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SQLInjectionPrevention()
    ex.show()
    sys.exit(app.exec_())