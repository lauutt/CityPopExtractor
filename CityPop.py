import os
import shutil
import zipfile
import rarfile

directory = 'download/'
temporary = 'tmp/'
music_directory = 'music/'
files = os.listdir(directory)
for file in files:
	file_directory = os.path.join(directory, file)
	print(file_directory)
	if file.endswith('.rar'):
		rar_ref = rarfile.RarFile(file_directory, 'r')
		rar_ref.extractall(temporary)
		rar_ref.close()
		print("Successfull Temp Unrar: "+str(file))
	elif file.endswith('.zip'):
		zip_ref = zipfile.ZipFile(file_directory, 'r')
		zip_ref.extractall(temporary)
		zip_ref.close()
		print("Successfull Temp Unzip: "+str(file))
	else: 
		print('Not able to unzip: '+str(file))


temp_folder = os.listdir(temporary)
for folder in temp_folder:
	path = temporary+folder
	if os.path.isdir(path):	
		in_folder = os.listdir(path)
		for file in in_folder:
			file_path = os.path.join(path, file)
			if file.endswith('.rar'):
				rar_ref = rarfile.RarFile(file_path, 'r')
				rar_ref.extractall(music_directory)
				print(rar_ref.printdir())
				rar_ref.close()

			elif file.endswith('.zip'):
				zip_ref = zipfile.ZipFile(file_path, 'r')
				zip_ref.extractall(music_directory)
				zip_ref.close()
				print("Successfull Final Unzip: "+str(file))
			else: 
				print('Not able to unzip: '+str(file))

shutil.rmtree(temporary)
	

