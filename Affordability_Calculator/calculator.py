import sys

from PyQt5.QtCore import Qt
#Importing QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar
from PyQt5.QtWidgets import QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QDialog, QDialogButtonBox

#Create class window from parent class QMainWindow
class CalcUI(QMainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle('Calculator')
		self.setFixedSize(435, 335)
		self.generalLayout = QVBoxLayout()
		self._centralWidget = QWidget(self)
		self.setCentralWidget(self._centralWidget)
		self._centralWidget.setLayout(self.generalLayout)
#Display
		self._createDisplay()
		self._createButtons()

		self._createMenu()
		self._createStatusBar()

	def _createDisplay(self):
		#Creating display widget
		self.display = QLineEdit()
		#Setting display properties
		self.display.setFixedHeight(35)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		self.generalLayout.addWidget(self.display)

	def _createButtons(self):
		self.buttons = {}
		buttonsLayout = QGridLayout()
		#Button text and layout
		buttons = {'By Hourly': (0,0),
					'By Net': (2,0),
					'By Gross': (3,0),
					'By Salary': (4,0),
			}
		for btnText, pos in buttons.items():
			self.buttons[btnText] = QPushButton(btnText)
			self.buttons[btnText].setFixedSize(40, 40)
			buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
		self.generalLayout.addLayout(buttonsLayout)

	def _createMenu(self):
		self.menu = self.menuBar().addMenu("&Menu")
		self.menu.addAction('Exit', self.close)


	def _createStatusBar(self):
		status = QStatusBar()
		status.addWidget(QPushButton('By Hourly'))
		status.addWidget(QPushButton('By Gross'))
		status.addWidget(QPushButton('By Net'))
		status.addWidget(QPushButton('By Salary'))
		self.setStatusBar(status)

if __name__ == '__main__':
	#instance of QApplication
	app = QApplication([])
	win = CalcUI()
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


