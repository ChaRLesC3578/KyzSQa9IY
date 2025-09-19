# 代码生成时间: 2025-09-19 17:28:31
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
Hash Calculator Application using Python and PyQt5.
This application allows users to input a string and calculates its hash using various hashing algorithms.
"""

class HashCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the user interface
        self.setWindowTitle('Hash Calculator')
        self.setGeometry(300, 300, 400, 300)

        # Layout
        self.layout = QVBoxLayout()

        # Input text edit
        self.inputTextEdit = QTextEdit(self)
        self.layout.addWidget(self.inputTextEdit)

        # Hash selection label
        self.hashLabel = QLabel('Select a hash algorithm:', self)
        self.layout.addWidget(self.hashLabel)

        # Hash selection combo box
        self.hashComboBox = QComboBox(self)
        self.hashComboBox.addItems(['MD5', 'SHA1', 'SHA256', 'SHA512'])
        self.layout.addWidget(self.hashComboBox)

        # Hash result label
        self.resultLabel = QLabel('Hash Result:', self)
        self.layout.addWidget(self.resultLabel)

        # Hash result text edit
        self.resultTextEdit = QTextEdit(self)
        self.resultTextEdit.setReadOnly(True)
        self.layout.addWidget(self.resultTextEdit)

        # Calculate button
        self.calculateButton = QPushButton('Calculate', self)
        self.calculateButton.clicked.connect(self.calculateHash)
        self.layout.addWidget(self.calculateButton)

        self.setLayout(self.layout)

    def calculateHash(self):
        # Get the input text and selected hash algorithm
        input_text = self.inputTextEdit.toPlainText()
        hash_algorithm = self.hashComboBox.currentText()

        # Calculate the hash
        try:
            hash_result = self.calculateTextHash(input_text, hash_algorithm)
            self.resultTextEdit.setText(hash_result)
        except Exception as e:
            self.resultTextEdit.setText(f'Error: {str(e)}')

    def calculateTextHash(self, text, algorithm):
        # Calculate the hash based on the selected algorithm
        if algorithm == 'MD5':
            return hashlib.md5(text.encode()).hexdigest()
        elif algorithm == 'SHA1':
            return hashlib.sha1(text.encode()).hexdigest()
        elif algorithm == 'SHA256':
            return hashlib.sha256(text.encode()).hexdigest()
        elif algorithm == 'SHA512':
            return hashlib.sha512(text.encode()).hexdigest()
        else:
            raise ValueError('Unsupported hash algorithm')

def main():
    app = QApplication(sys.argv)
    ex = HashCalculator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()