# 代码生成时间: 2025-08-31 23:42:19
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel
from PyQt5.QtCore import QProcess


class DocumentConverter(QWidget):
    """
    文档格式转换器界面
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化界面
        """
        self.setWindowTitle('Document Converter')
        self.setGeometry(300, 300, 300, 120)

        self.label = QLabel('Select a document to convert:', self)
        self.label.move(20, 20)

        self.browse_button = QPushButton('Browse', self)
        self.browse_button.move(20, 50)
        self.browse_button.clicked.connect(self.browse_file)

        self.show()

    def browse_file(self):
        """
        浏览文件并选择文档
        """
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'All Files (*);;Word Documents (*.docx)', options=options)
        if filename:
            self.convert_document(filename)

    def convert_document(self, filename):
        """
        将文档转换为PDF
        """
        try:
            # 使用LibreOffice命令行工具进行转换
            # 请确保LibreOffice已安装，并且soffice命令可用
            process = QProcess(self)
            process.start('libreoffice', ['--convert-to', 'pdf', '--headless', filename])
            process.waitForFinished()
            if process.exitCode() == 0:
                print(f'Document converted successfully: {filename}')
            else:
                raise Exception('Failed to convert document')
        except Exception as e:
            print(f'Error: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = DocumentConverter()
    sys.exit(app.exec_())