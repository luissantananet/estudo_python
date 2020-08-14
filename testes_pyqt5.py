import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('First App')
window.show()
sys.exit(app.exec_())
