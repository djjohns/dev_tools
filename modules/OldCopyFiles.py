import os
import shutil
import time
import threading
from playsound import playsound


class CopyFiles():
    '''
    ### Copy files form a source directory where the filename ends with a passed
    file extension to a destination directory.
    
    #### Args:
    source_dir (str): The directory we want to copy files from. EG: a flashdrive,
    mapped network drive such as "Z:/"
    
    dest_dir (str): The directory we want to copy files to. EG: a flashdrive,
    or real path such as "C:/FileDump"
    
    file_type (str): The file type to copy. EG: ".csv"
    #### Implementation example:
    ```
    copy_csv_files = CopyFiles(
        source_dir="E:/",
        dest_dir="C:/FileDump",
        file_type=".csv"
        )
    copy_csv_files
    ```
    '''
    def __init__(self, source_dir=None, dest_dir=None, file_type=None):
        self.source_dir = os.path.realpath(source_dir)
        self.dest_dir = os.path.realpath(dest_dir)
        self.file_type = file_type
        try:
            def loading():
                threading.Thread(target=playsound, args=("../audio/loading.wav",), daemon=True).start()
            # def done():
                # threading.Thread(target=playsound, args=("../audio/confirmation.wav",), daemon=True).start()
            # Iterate through the files within the passed source directory.
            for filename in os.listdir(self.source_dir):
                # If file ends with passed file_type.
                if filename.endswith(self.file_type):
                    loading()
                    filesize = os.path.getsize(os.path.join(self.source_dir,filename))  # Get size of file in bytes
                    print(f"Copying {filename} from {self.source_dir} to {self.dest_dir}.")
                    shutil.copy(os.path.join(self.source_dir, filename), self.dest_dir)
                else:
                    print(f"No files ending in {self.file_type} found in {self.source_dir}.")
                    continue
            for _ in range(3):
                playsound('../audio/confirmation.wav')
                # done()
                time.sleep(0.1)
        except Exception as e:
            print(f"Error copying from {self.source_dir} to {self.dest_dir}.")
            print(e)

if __name__ == '__main__':
    copy_csv_files = CopyFiles(
        source_dir="C:/dev/test/",
        dest_dir="C:/dev/file_dump",
        file_type=".csv"
    )
    copy_csv_files