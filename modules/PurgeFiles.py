import os


class PurgeFiles():
    '''
    ### Delete files form a source directory where the filename ends with a passed
    file extension.
    
    #### Args:
    source_dir (str): The directory we want to purge files from. EG: a flashdrive,
    mapped network drive such as "Z:/"
    
    file_type (str): The file type to purge. EG: ".csv"
    #### Implementation example:
    ```
    purge_files = PurgeFiles(
        source_dir="C:/dev/test/",
        file_type=".csv"
    )
    purge_files
    ```
    '''
    def __init__(self, source_dir=None, file_type=None):
        self.source_dir = os.path.realpath(source_dir)
        self.file_type = file_type
        try:
            # Iterate through the files within the passed source directory.
            for filename in os.listdir(self.source_dir):
                # If file ends with passed file_type.
                if filename.endswith(self.file_type):
                    os.remove(os.path.join(self.source_dir,filename)),
                    print(f"Purging {filename} from {self.source_dir}.")
                else:
                    print(f"No files ending in {self.file_type} found in {self.source_dir}.")
                    continue
        except Exception as e:
            print(f"Error purging from {self.source_dir} to {self.dest_dir}.")
            print(e)

if __name__ == '__main__':
    purge_files = PurgeFiles(
        source_dir="C:/dev/test/",
        file_type=".csv"
    )
    purge_files