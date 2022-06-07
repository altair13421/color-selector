import os
import json

class ColorSelectorBack():
	def __init__(self):
		pass
	def save_file(self, colorDict):
		if not os.path.exists(os.path.join('.', 'ColorSelector_files')):
			os.mkdir('ColorSelector_files')
		os.chdir(os.path.join('.', 'ColorSelector_files'))
		with open(f"color.json", 'w') as fileWrite:
			fileWrite.write(json.dumps(colorDict, sort_keys = True, indent = 4))
		os.chdir('..')
		pass
	
	pass
pass
