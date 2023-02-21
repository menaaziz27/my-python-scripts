import os 
import shutil

current_path = os.path.dirname(os.path.realpath(__file__))
print(current_path)
try :
	print('Welcome in organising-folders script!\nI\'m here to help you!')

	#Check if files are images
	for file in os.listdir(current_path):
		if file.lower().endswith(('.jpg', '.png', 'jpeg', '.gif', ".bmp", ".pbm", ".pnm" )):
			if not os.path.exists('Images'):
				os.mkdir('Images')
			shutil.copy2(file , 'Images')
			os.remove(file)

		if file.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")):
			if not os.path.exists('Music'):
				os.mkdir('Music')
			shutil.copy2(file , 'Music')
			os.remove(file)

		if file.endswith((".webm", ".mp4" ,'.MOV')):
			if not os.path.exists('video'):
				os.mkdir('video')
			shutil.copy2(file , 'video')
			os.remove(file)

		if file.lower().endswith((".exe", ".msi", ".deb" , "dmg")):
			if not os.path.exists('executables'):
				os.mkdir('executables')
			shutil.copy2(file , 'executables')
			os.remove(file)

		if file.lower().endswith((".rar", ".tar" , ".zip" , ".gz")):
			# If archive folder doesnt exist then create
			if not os.path.exists('archives'):
				os.mkdir('archives')
			shutil.copy2(file , 'archives')
			os.remove(file)

		if file.lower().endswith('.torrent'):
			if not os.path.exists('torrent'):
				os.mkdir('torrent')
			shutil.copy2(file , 'torrent')
			os.remove(file)

		if file.lower().endswith((".py", ".php", ".html" , ".css" , ".js")):
			if not os.path.exists('code'):
				os.mkdir('code')
			shutil.copy2(file , 'code')
			os.remove(file)

		if file.lower().endswith((".txt", ".pdf", ".docx" , "doc",'.ppt','.pptx')):
			if not os.path.exists("documents"):
				os.makedirs("documents")
			shutil.copy2(file, "documents")
			os.remove(file)

except OSError: 
	print('Error')

finally:

	os.system('cls' if os.name == 'nt' else 'clear')

	print('All done!\nhappy clean folders babe (:')
