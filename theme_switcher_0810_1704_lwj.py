# 代码生成时间: 2025-08-10 17:04:01
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog
from PyQt5.QtCore import Qt

"""
A PyQt5 application that allows users to switch themes.
"""

class ThemeSwitcher(QWidget):
    """
    A class representing a simple GUI with a button to switch themes.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface components.
        """
        self.setWindowTitle('Theme Switcher')
        self.setGeometry(300, 300, 300, 200)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a button to switch themes
        self.btn_switch_theme = QPushButton('Switch Theme', self)
        self.btn_switch_theme.clicked.connect(self.switch_theme)

        # Add the button to the layout
        layout.addWidget(self.btn_switch_theme)

        # Set the layout for the main window
        self.setLayout(layout)

    def switch_theme(self):
        """
        Switches the theme of the application by opening a color dialog.
        """
        # Open a color dialog and get the selected color
        color = QColorDialog.getColor()
        if color.isValid():
            # Set the background color of the application
            self.setStyleSheet(f"QWidget {{ background-color: {color.name()}; }}")
        else:
            # Handle the case where the user cancels the color dialog
            print("Theme switch cancelled.")


def main():
    """
    The main function that runs the application.
    """
    app = QApplication(sys.argv)
    window = ThemeSwitcher()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
