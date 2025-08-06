# 代码生成时间: 2025-08-06 20:00:37
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox

class JsonConverterApp(QWidget):
    """A PyQt5 application to convert JSON data between different formats."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initializes the application's UI components."""
        self.setWindowTitle('JSON Data Format Converter')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.inputTextEdit = QTextEdit(self)
        self.inputTextEdit.setPlaceholderText('Paste your JSON data here...')
        layout.addWidget(self.inputTextEdit)

        self.outputTextEdit = QTextEdit(self)
        self.outputTextEdit.setPlaceholderText('Formatted JSON will appear here...')
        self.outputTextEdit.setReadOnly(True)
        layout.addWidget(self.outputTextEdit)

        self.convertButton = QPushButton('Convert', self)
        self.convertButton.clicked.connect(self.convertJson)
        layout.addWidget(self.convertButton)

        self.setLayout(layout)

    def convertJson(self):
        """Converts the input JSON data to a formatted string and displays it."""
        input_data = self.inputTextEdit.toPlainText()
        try:
            data = json.loads(input_data)
            formatted_json = json.dumps(data, indent=4)
            self.outputTextEdit.setText(formatted_json)
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, 'Error', f'Invalid JSON data: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JsonConverterApp()
    ex.show()
    sys.exit(app.exec_())