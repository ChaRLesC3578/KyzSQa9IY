# 代码生成时间: 2025-09-12 11:03:06
# theme_switcher.py
# This program demonstrates a theme switcher using the PyQt framework.

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon, QColor

class MainWindow(QMainWindow):
    # Class to create the main window
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize the UI components
        self.setWindowTitle('Theme Switcher')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon('icon.png'))

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a button to switch themes
        self.button = QPushButton('Switch Theme', self)
        self.button.clicked.connect(self.switchTheme)

        # Add the button to the layout
        layout.addWidget(self.button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Load the saved theme color
        self.loadThemeColor()

    def switchTheme(self):
        # Function to switch between two themes
        try:
            # Check if the current theme is light or dark
            if self.button.styleSheet() == '':
                # Set the dark theme
                self.setDarkTheme()
            else:
                # Set the light theme
                self.setLightTheme()
        except Exception as e:
            print(f'Error switching theme: {e}')

    def setLightTheme(self):
        # Function to set the light theme
        self.setStyleSheet('')
        self.button.setStyleSheet('QPushButton { background-color: #F0F0F0; }')
        self.saveThemeColor('light')

    def setDarkTheme(self):
        # Function to set the dark theme
        self.setStyleSheet('QWidget { background-color: #333; color: white; }')
        self.button.setStyleSheet('QPushButton { background-color: #555; color: white; }')
        self.saveThemeColor('dark')

    def loadThemeColor(self):
        # Function to load the theme color from settings
        settings = QSettings('ThemeSwitcher', 'Settings')
        theme_color = settings.value('theme_color', 'light')
        if theme_color == 'dark':
            self.setDarkTheme()
        else:
            self.setLightTheme()

    def saveThemeColor(self, theme_color):
        # Function to save the theme color to settings
        settings = QSettings('ThemeSwitcher', 'Settings')
        settings.setValue('theme_color', theme_color)

# Main function to run the application
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
