# 代码生成时间: 2025-08-05 02:59:33
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt
import psutil

# 定义一个进程模型
class ProcessTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.processes = []
        self.columns = ["PID", "Process Name", "Memory(%)", "CPU(%)"]

    def rowCount(self, parent=None):
        return len(self.processes)

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            process = self.processes[index.row()]
            return getattr(process, self.columns[index.column()].lower())
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.columns[section]
        return None

    def refresh(self):
        self.beginResetModel()
        self.processes = [psutil.Process(pid) for pid in psutil.pids()]
        self.endResetModel()

# 进程管理器界面
class ProcessManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Process Manager')
        self.setGeometry(100, 100, 800, 600)

        self.model = ProcessTableModel()
        self.table = QTableWidget()
        self.table.setModel(self.model)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)

        self.start_button = QPushButton('Refresh')
        self.start_button.clicked.connect(self.refresh_table)
        self.layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def refresh_table(self):
        self.model.refresh()
        self.table.viewport().update()

# 主函数
def main():
    app = QApplication(sys.argv)
    manager = ProcessManager()
    manager.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()