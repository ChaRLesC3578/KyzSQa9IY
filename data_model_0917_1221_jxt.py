# 代码生成时间: 2025-09-17 12:21:43
import sys
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QTableView

"""
A simple data model for demonstration purposes in PyQt.
This model will hold a list of data items and expose them to a view.
"""

class DataModel(QAbstractTableModel):
    """PyQt Table Model for demonstration purposes."""

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data  # Internal data storage

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in the model."""
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the model."""
        if not self._data:
            return 0
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        """Return the data stored under the given index for the specified role."""
        if index.isValid() and role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the header data for the specified section and orientation."""
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return f"Column {section + 1}"
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """Set the data for the given index to the value."""
        if index.isValid() and role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def insertRows(self, position, rows, index=QModelIndex()):
        """Insert rows into the model."""
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for _ in range(rows):
            self._data.insert(position, [])
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, index=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        for _ in range(rows):
            self._data.pop(position)
        self.endRemoveRows()
        return True

    def flags(self, index):
        """Return the item flags for the given index."""
        return super().flags(index) | Qt.ItemIsEditable

# Example usage of the DataModel
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Sample data
    data = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
    model = DataModel(data)
    view = QTableView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec_())