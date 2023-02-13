import os
import shutil
import time
import threading
from playsound import playsound
from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class MoveFiles():
    '''
    ### Moves files from a source path to a destination path.
    #### Args:
    source_dir (str): Path to source dir of files you want to move.
    dest_dit (str): Path to destination dir of where you want to move the files to.
    file_type (str): File extention of the files you want to move.
    '''
    source_dir: str
    dest_dir: str
    file_type: str

    def _move_complete(self):
        for _ in range(3):
                playsound('../audio/confirmation.wav')
                time.sleep(0.1)

    # TODO: implement if file count/filesize threshold is met.
    def _loading_sound(self):
        threading.Thread(
            target=playsound,
            args=("../audio/loading.wav",),
            daemon=True
        ).start()


    def move(self):
        '''
        Moves files from source to destination.
        '''
        for filename in tqdm(
            # Use tqdm for progress bar.
            os.listdir(self.source_dir),  # Iterable, 
            unit =f" {self.file_type} files",  # Set our unit of measure.
            desc = f"Moving files to {self.dest_dir}"  # Set our description.
        ):
            # If filename ends with specified file type.
            if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                # Move files from source to destination.
                shutil.move(os.path.join(self.source_dir, filename), self.dest_dir)
                time.sleep(0.1)  # Sleep to so progress in progress bar.
        self._move_complete()  # Play our alert sound.


    def move_recursively(self):
        for root, dirs, files in os.walk(self.source_dir):
            for filename in tqdm(
                # Use tqdm for progressbar.
                files,  # Iterable of files.
                unit =f" {self.file_type} files",  # Set our unit of measure.
                desc = f"Moving files to {self.dest_dir}."  # Set our description. 
            ):
                # If filename ends with specified file_type.
                if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                    # Move files from source to destination.
                    shutil.move(os.path.join(root, filename), self.dest_dir)
                    time.sleep(0.1)  # Sleep to show progress in progress bar.
        self._move_complete()  # Play our alert sound.



if __name__ == '__main__':
    move_stl_files = MoveFiles(
    "C:/Users/djjoh/Downloads/",  # Source
    "C:/Users/djjoh/OneDrive/stl_files/",  # Destination
    ".stl"  # File type
)
    move_stl_files.move()
    # move_stl_files.move_recursively()