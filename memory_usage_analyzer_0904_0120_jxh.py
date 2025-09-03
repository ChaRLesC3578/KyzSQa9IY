# 代码生成时间: 2025-09-04 01:20:12
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont

class MemoryUsageAnalyzer(QMainWindow):
    """
    A PyQt5 application for displaying system memory usage.
    """
    def __init__(self):
        super().__init__()
        self.title = 'Memory Usage Analyzer'
        self.initUI()

    def initUI(self):
        """
        Initialize the main window and setup the UI components.
        """
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set it as the main widget of the window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout
        layout = QVBoxLayout(central_widget)

        # Create a label to display memory usage
        self.memory_usage_label = QLabel('Memory Usage: 0%')
        self.memory_usage_label.setFont(QFont('Arial', 14))
        layout.addWidget(self.memory_usage_label)

        # Start the memory usage update loop
        self.update_memory_usage()

    def update_memory_usage(self):
        """
        Update the memory usage label text with the current system memory usage.
        """
        try:
            # Get the memory usage percentage
            memory = psutil.virtual_memory()
            usage_percent = memory.percent

            # Update the label with the current memory usage
            self.memory_usage_label.setText(f'Memory Usage: {usage_percent}%')
        except Exception as e:
            # Handle any exceptions that occur during memory usage retrieval
            self.memory_usage_label.setText(f'Error: {e}')
        finally:
            # Schedule the next update after 1 second
            self.timer = self.startTimer(1000)

    def timerEvent(self, event):
        """
        Timer event handler to periodically update the memory usage.
        """
        if event.timerId() == self.timer:
            self.killTimer(self.timer)
            self.update_memory_usage()
            self.timer = self.startTimer(1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    analyzer = MemoryUsageAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())