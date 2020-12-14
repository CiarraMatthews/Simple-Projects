import sys

#Importing QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton 

#instance of QApplication
app = QApplication([])

#instance of application's GUI
window = QWidget()
window.setWindowTitle('Calculator')

#Layout
layout = QHBoxLayout()
layout.addWidget(QPushButton('By Hourly'))
layout.addWidget(QPushButton('By Monthly'))
layout.addWidget(QPushButton('By Salary'))
window.setLayout(layout)

window.setGeometry(800, 700, 780, 580)
window.move(60, 15)
#message = QLabel('<h1>Hello World!</h1>', parent = window)
#message.move(60, 15)

#shows the application' GUI
window.show()

#main loop
sys.exit(app.exec_())
