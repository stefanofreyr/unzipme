import zipfile

def extract_archive(filepath, destination_dir):
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(destination_dir)
