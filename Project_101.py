import dropbox
import os

class Uploading:
    def __init__(self, accessCode, source, destination):
        self.accessCode = accessCode
        self.destination = destination
        self.source = source
    
    def uploadFiles(self):
        dbx = dropbox.Dropbox(self.accessCode)



        for root, dirs, files in os.walk(self.source):
            for name in files:
                if name == '.DS_Store':
                    os.remove(os.path.join(root, name))
                    continue
                else:
                    localPath = os.path.join(root, name)
                    relativePath = os.path.relpath(localPath, self.source)
                    remotePath = os.path.join(self.destination, relativePath)

                    with open(localPath, 'rb') as f:
                        dbx.files_upload(f.read(), remotePath, mode = dropbox.files.WriteMode.overwrite)

def main():
    code = input('Please enter your dropbox access code... ')
    originalFile = input('Please enter the path of the folder you want to upload... ')
    dropboxDestination = input('Please enter the path of the dropbox location you would like to upload to... ')

    uploader = Uploading(code, originalFile, dropboxDestination)
    uploader.uploadFiles()

    print('Your item has been uploaded.')

main()