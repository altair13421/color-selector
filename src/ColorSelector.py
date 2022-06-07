#!/usr/bin/python
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QColor
import ColorSelector_back as co

class MainColorSelectorWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUi()
		self.backObj = co.ColorSelectorBack()
		pass
	
	def initializeUi(self):
		self.setGeometry(500, 200, 350, 350)
		self.setWindowTitle('ColorSelector')
		self.view_all_widgets()
		self.show()
		pass
	
	def view_all_widgets(self):
		formLayout = QFormLayout()
		titleLabel = QLabel()
		titleLabel.setText("ColorSelector")
		titleLabel.setFont(QFont('Whitney', 16))
		titleLabel.setAlignment(Qt.AlignCenter)
		
		formLayout.setContentsMargins(10,30,10,70)
		formLayout.setSpacing(20)
		
		self.alphaEntry = QLineEdit()
		self.redEntry = QLineEdit()
		self.greenEntry = QLineEdit()
		self.blueEntry = QLineEdit()
		
		selectColorButton = QPushButton("Select Color")
		clearButton = QPushButton("Clear Entries")
		
		selectColorButton.clicked.connect(self.select_color)
		clearButton.clicked.connect(self.clear_entries)
		
		formLayout.addRow(titleLabel)
		formLayout.addRow('Alpha Value: ', self.alphaEntry)
		formLayout.addRow("Red Value: ", self.redEntry)
		formLayout.addRow("Green Value: ", self.greenEntry)
		formLayout.addRow("Blue Value: ", self.blueEntry)
		formLayout.addRow(selectColorButton)
		formLayout.addRow(clearButton)
		
		self.alphaEntry.setReadOnly(True)
		self.redEntry.setReadOnly(True)
		self.greenEntry.setReadOnly(True)
		self.blueEntry.setReadOnly(True)
		
		self.setLayout(formLayout)
		pass
	
	def select_color(self):
		color = QColorDialog.getColor()
		colorDict = {"red": color.red(), "green": color.green(), "blue": color.blue(), "alpha": color.alpha(), 'rgba': color.getRgb()}
		self.backObj.save_file(colorDict)
		self.alphaEntry.setText(str(color.alpha()))
		self.redEntry.setText(str(color.red()))
		self.greenEntry.setText(str(color.green()))
		self.blueEntry.setText(str(color.blue()))
		pass
	
	def clear_entries(self):
		self.alphaEntry.clear()
		self.redEntry.clear()
		self.greenEntry.clear()
		self.blueEntry.clear()
		pass
	pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainColorSelectorWindow()
	sys.exit(app.exec_())
	pass
