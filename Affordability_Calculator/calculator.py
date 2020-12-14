import sys

#Importing QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

#instance of QApplication
app = QApplication([])

#instance of application's GUI
window = QWidget()
window.setWindowTitle('Calculator')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
message = QLabel('<h1>Hello World!</h1>', parent = window)
message.move(60, 15)

#shows the application' GUI
window.show()

#main loop
sys.exit(app.exec_())
