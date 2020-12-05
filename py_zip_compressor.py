from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from zipfile import ZipFile 
import sys

class Window(QtWidgets.QWidget):
	"""docstring for Window"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.file_path = []
		self.setWindowTitle("Zip Compressor")
		self.setGeometry(100, 100, 300, 80)  
		self.ui()
		self.show()

	def ui(self):
		self.label_1 = QLabel("Enter the file name to save the zip")

		self.select_btn = QPushButton('Browse..',self)
		self.download_btn = QPushButton('Download')
		self.type_space = QLineEdit('files.zip')
		
		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(self.type_space)
		hbox.addWidget(self.select_btn)
		hbox.addWidget(self.download_btn)
		
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addWidget(self.label_1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)
		

		self.select_btn.clicked.connect(lambda x : self.handleButton() )
		self.download_btn.clicked.connect(lambda x : self.Download_zip())
		

	def handleButton(self):
		title = self.select_btn.text()
		self.file_path = QFileDialog.getOpenFileNames(self, title)
		self.file_path = self.file_path[0]
		
	def Download_zip(self):
		file_name = self.type_space.text()
		print(self.file_path)
		with ZipFile(file_name,'w') as zip:
			for file in self.file_path:
				zip.write(file)

		

		
if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())