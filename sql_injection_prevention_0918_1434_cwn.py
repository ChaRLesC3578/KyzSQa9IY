# 代码生成时间: 2025-09-18 14:34:12
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sqlite3

"""
A PyQt5 application to demonstrate prevention of SQL injection attacks.
This application uses parameterized queries to ensure that SQL injection cannot occur.
"""

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to execute a parameterized query to prevent SQL injection
def parameterized_query(conn, query, params):
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Main application class
class SQLInjectionPreventionApp(QWidget):
    def __init__(self, db_file):
        super().__init__()
        self.init_ui(db_file)

    def init_ui(self, db_file):
        # Create the database connection
        self.conn = create_connection(db_file)

        # Create the GUI elements
        self.username_label = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        # Layout configuration
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Set the window title
        self.setWindowTitle('SQL Injection Prevention')
        self.show()

    def login(self):
        # Retrieve user input
        username = self.username_input.text()
        password = self.password_input.text()

        # Create a parameterized query to prevent SQL injection
        query = 'SELECT * FROM users WHERE username=? AND password=?'
        params = (username, password)

        # Execute the query
        parameterized_query(self.conn, query, params)

        # Check if the user exists
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()

        if result:
            self.show_message('Login successful!')
        else:
            self.show_message('Invalid username or password!')

    def show_message(self, message):
        # Show a message to the user
        print(message)

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    db_file = 'example.db'
    ex = SQLInjectionPreventionApp(db_file)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()