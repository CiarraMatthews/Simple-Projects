import sys

#Importing QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QDialog, QDialogButtonBox

#Instance of application's GUI rite?
class Window(QMainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle('Calculator')
		self.setCentralWidget(QLabel("Central Widget"))
		self._createMenu()
		self._createToolBar()
		self._createStatusBar()

	def _createMenu(self):
		self.menu = self.menuBar().addMenu("&Menu")
		self.menu.addAction('Exit', self.close)

	def _createToolBar(self):
		tools = QToolBar()
		self.addToolBar(tools)
		tools.addAction('Exit', self.close)

	def _createStatusBar(self):
		status = QStatusBar()
		status.showMessage("I'm the Status Bar")
		self.setStatusBar(status)

if __name__ == '__main__':
	#instance of QApplication
	app = QApplication([])
	win = Window()
	#shows the application's GUI
	win.show()
	#main loop
	sys.exit(app.exec_())

#Layout of buttons
#layout = QHBoxLayout()
#layout.addWidget(QPushButton('By Hourly'))
#layout.addWidget(QPushButton('By Monthly'))
#layout.addWidget(QPushButton('By Salary'))
#window.setLayout(layout)

#Layout of Forms
#layout2 = QFormLayout()
#layout2.addRow('Hourly Income', QLineEdit())
#layout2.addRow('Hours per Week', QLineEdit())
#window.setLayout(layout2)

#window.setGeometry(800, 700, 780, 580)
#window.move(60, 15)


