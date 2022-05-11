import os
import shutil
import time
import threading
from playsound import playsound
from dataclasses import dataclass


@dataclass
class CopyFiles():
    source_dir: str
    dest_dir: str
    file_type: str

    def _copy_complete(self):
        for _ in range(3):
                playsound('../audio/confirmation.wav')
                time.sleep(0.1)

    def _loading_sound(self):
        threading.Thread(
            target=playsound,
            args=("../audio/loading.wav",),
            daemon=True
        ).start()

    def copy(self):
        for filename in os.listdir(self.source_dir):
            if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                print(f"Copying {filename} from {self.source_dir} to {self.dest_dir}.")
                shutil.copy(os.path.join(self.source_dir, filename), self.dest_dir)
        self._copy_complete()

    def copy_recursively(self):
        for root, dirs, files in os.walk(self.source_dir):
            for filename in files:
                if filename.endswith(self.file_type.lower()) or filename.endswith(self.file_type.upper()):
                    print(f"Copying {filename} from {root} to {self.dest_dir}.")
                    shutil.copy(os.path.join(root, filename), self.dest_dir)
        self._copy_complete()



if __name__ == '__main__':
    copy_csv_files = CopyFiles(
        "C:/dev/test/", # source directory
        "C:/dev/file_dump", # destination directory
        ".csv", # file type
    )
    copy_csv_files.copy()
    copy_csv_files.copy_recursively()