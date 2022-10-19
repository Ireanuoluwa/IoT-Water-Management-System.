import os
import shutil



temp_filepath = input("Enter the directory path:  ")

dest_images = temp_filepath + '\Images'
dest_zip = temp_filepath + '\Zip'
dest_vid = temp_filepath + '\Video'
dest_documents = temp_filepath + '\Documents'
dest_programs = temp_filepath + '\Programs'
dest_others = temp_filepath + '\Others'

def new_dir():
    """
    Creates new folders (documents, videos, compressed and images.)
    
    """
    os.mkdir(dest_documents)
    os.mkdir(dest_vid)
    os.mkdir(dest_zip)
    os.mkdir(dest_programs)
    os.mkdir(dest_images)
    
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]


document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd",".mkv"]


zip_extensions = [".zip", ".zipx", ".rar"]
                    


class manage_files():

    """
    Checks the directory for their file extensions and arranges them according to their file extensions to their corresponding folders.
    
    """


    def __init__(self):
        self.file_path = temp_filepath
        files = os.listdir(self.file_path)
        for file in files:
            self.check_document(file)
            self.check_compressed(file)
            self.check_video(file)
            self.check_images(file)
    


    def check_document(self,file):
        for docs in document_extensions:
            if "." in file:
                if file.endswith(docs):
                    shutil.move(temp_filepath+'/'+file,dest_documents)
    def check_compressed(self,file):
        for zip in zip_extensions:
            if "." in file:
                if file.endswith(zip):
                    shutil.move(temp_filepath+'/'+file,dest_zip)

    def check_video(self,file):
        for vid in video_extensions:
            if "." in file:
                if file.endswith(vid):
                    shutil.move(temp_filepath+'/'+file,dest_vid)

    def check_images(self,file):
        for img in image_extensions:
            if "." in file:
                if file.endswith(img):
                    shutil.move(temp_filepath+'/'+file,dest_images)
        

new_dir()
ArrangeFiles = manage_files()