# import shutil
# importing the requests module
import requests
print('Downloading started')
url = 'https://demo-workspace.a4.saagie.io/projects/api/platform/2/project/db844ca5-4041-4661-917d-0ba8ea6dd086/job/95c6aebe-339a-436d-811a-cc8e200ef042/version/2/artifact/test.py'

# Downloading the file by sending the request to the URL
req = requests.get(url)
 
# Split URL to get the file name
filename = url.split('/')[-1]
 
# Writing the file to the local file system
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

#Compression en .zip d'un DOSSIER venant d'un autre chemin
# shutil.make_archive(r'C:\Users\elied\Downloads\ctrlC-ctrlV-hackathon-backend-develop\ctrlC-ctrlV-hackathon-backend-develop\Backend\backend\Test projet\TestA','zip',r'https://demo-workspace.a4.saagie.io/projects/api/platform/2/project/db844ca5-4041-4661-917d-0ba8ea6dd086/job/95c6aebe-339a-436d-811a-cc8e200ef042/version/2/artifact/test.py')



# import zipfile


# zfile = zipfile.ZipFile('nombres.zip', 'w', compression=zipfile.ZIP_DEFLATED) #Création de nombres.zip en données transparentes
# zfile.writestr('Test projet\ProjetA.txt')
# zfile.writestr('Test projet\ProjetB.txt')
# zfile.close()


