import os
import shutil
import time
import threading
from playsound import playsound
from dataclasses import dataclass
from tqdm import tqdm


@dataclass
class CopyFiles():
    source_dir: str
    dest_dir: str
    file_type: str

    def _copy_complete(self):
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


    def copy(self):
        for filename in tqdm(
            # Use tqdm for progress bar.
            os.listdir(self.source_dir),  # Iterable, 
            unit =f" {self.file_type} files",  # Set our unit of measure.
            desc = f"Copying files to {self.dest_dir}"  # Set our description.
        ):
            # If filename ends with specified file type.
            if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                # Copy files from source to destination.
                shutil.copy(os.path.join(self.source_dir, filename), self.dest_dir)
                time.sleep(0.1)  # Sleep to so progress in progress bar.
        self._copy_complete()  # Play our alert sound.


    def copy_recursively(self):
        for root, dirs, files in os.walk(self.source_dir):
            for filename in tqdm(
                # Use tqdm for progressbar.
                files,  # Iterable of files.
                unit =f" {self.file_type} files",  # Set our unit of measure.
                desc = f"Copying files to {self.dest_dir}."  # Set our description. 
            ):
                # If filename ends with specified file_type.
                if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                    # Copy files from source to destination.
                    shutil.copy(os.path.join(root, filename), self.dest_dir)
                    time.sleep(0.1)  # Sleep to show progress in progress bar.
        self._copy_complete()  # Play our alert sound.



if __name__ == '__main__':
    copy_csv_files = CopyFiles(
        "C:/dev/test/", # source directory
        "C:/dev/file_dump", # destination directory
        ".csv", # file type
    )
    # copy_csv_files.copy()
    copy_csv_files.copy_recursively()