import os
import glob
import csv

class BulkRename:

	def __init__(self, folder_path: str, name_file: list):
		
		self.folder_path = folder_path
		self.files = glob.glob(self.folder_path)
		self.name_file = name_file
		if not self.files:
			raise Exception('No files found, please check folder path')	
		try:
			with open(name_file, 'r') as f:
				reader = csv.reader(f)
				self.name_dict = {key : value for key, value in reader}
				# print(self.name_dict)
		except FileNotFoundError as e:
			print('Name file not found, please check the file name and file path')

	@property
	def folder_path(self):
		return self._folder_path

	@folder_path.setter
	def folder_path(self, folder_path):
		if folder_path[-1] == '/':
			folder_path += '*'
		elif folder_path[-1] != '/' and folder_path[-1] != '*':
			folder_path += '/*'
		self._folder_path = folder_path
	

	def rename(self):
		for file in self.files:
			path = ''.join(file.split('/')[:-1]) + '/'
			# import pdb;pdb.set_trace()
			filename = file.split('/')[-1]
			# import pdb;pdb.set_trace()
			if filename in self.name_dict.keys():
				os.rename(file, path + self.name_dict[filename])
				print(f'filename changed for {filename}, new name: {self.name_dict[filename]}')
			else:
				print(f'filename not changed for {filename}, no new filename found in {self.name_file}')

if __name__ == '__main__':
	file_renamer = BulkRename('test/*', 'test/name_file.csv')
	file.rename()