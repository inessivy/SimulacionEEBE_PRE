import sys

from PyQt5.QtCore import Qt, QEvent, QObject
from PyQt5.QtWidgets import QApplication

from MVP.ConfigPrincipal import MainWindow


class KeyPressFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                obj.currentWidget().escKeyPressEvent()
        return super().eventFilter(obj, event)


app = QApplication([])
qapp = MainWindow()
qapp.main()
qapp.show()
sys.exit(app.exec())

