from MoveFiles import MoveFiles


move_stl_files = MoveFiles(
    "C:/Users/djjoh/Downloads/",  # Source
    "C:/Users/djjoh/OneDrive/stl_files/",  # Destination
    ".stl"  # File type
)

move_stl_files.move()
