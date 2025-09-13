# 代码生成时间: 2025-09-14 07:08:23
import sys
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit
from PyQt5.QtCore import Qt
import mysql.connector
from mysql.connector import Error
import os
from mysqldump import mysqldump

"""
Database Migration Tool using Python and PyQt5.
This tool allows users to migrate databases from one MySQL server to another.
"""

class DatabaseMigrationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Database Migration Tool')
        self.setGeometry(100, 100, 600, 400)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the source database label and text edit
        self.source_db_label = QLabel('Source Database Connection Details:')
        self.source_db_text = QTextEdit()
        self.source_db_text.setPlaceholderText('Enter source database connection details in the format:
host,user,password,database')

        # Create the target database label and text edit
        self.target_db_label = QLabel('Target Database Connection Details:')
        self.target_db_text = QTextEdit()
        self.target_db_text.setPlaceholderText('Enter target database connection details in the format:
host,user,password,database')

        # Create the migration button
        self.migrate_button = QPushButton('Migrate Database')
        self.migrate_button.clicked.connect(self.migrate_database)

        # Add widgets to the main layout
        main_layout.addWidget(self.source_db_label)
        main_layout.addWidget(self.source_db_text)
        main_layout.addWidget(self.target_db_label)
        main_layout.addWidget(self.target_db_text)
        main_layout.addWidget(self.migrate_button)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def migrate_database(self):
        # Get the source and target database connection details
        source_db_details = self.source_db_text.toPlainText().strip()
        target_db_details = self.target_db_text.toPlainText().strip()

        try:
            # Split the connection details into their respective components
            source_db_details = source_db_details.split(',')
            target_db_details = target_db_details.split(',')

            # Establish a connection to the source database
            self.source_db = mysql.connector.connect(
                host=source_db_details[0],
                user=source_db_details[1],
                password=source_db_details[2],
                database=source_db_details[3]
            )
            self.source_cursor = self.source_db.cursor()

            # Establish a connection to the target database
            self.target_db = mysql.connector.connect(
                host=target_db_details[0],
                user=target_db_details[1],
                password=target_db_details[2],
                database=target_db_details[3]
            )
            self.target_cursor = self.target_db.cursor()

            # Get the database schema from the source database
            self.source_cursor.execute('SHOW TABLES')
            tables = self.source_cursor.fetchall()

            # Migrate each table from the source database to the target database
            for table in tables:
                table_name = table[0]
                mysqldump.dump_database(self.source_db, self.target_db, table_name)

            # Commit the changes and close the connections
            self.target_db.commit()
            self.source_db.close()
            self.target_db.close()

            # Display a success message
            logging.info('Database migration completed successfully.')

        except Error as e:
            # Handle any errors that occur during the migration process
            logging.error(f'Error migrating database: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DatabaseMigrationTool()
    main_window.show()
    sys.exit(app.exec_())