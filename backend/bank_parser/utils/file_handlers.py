import os
from django.core.files.storage import FileSystemStorage


def handle_uploaded_file(file) -> str:
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    return fs.path(filename)


def get_file_type(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1].lower()
    return ext[1:] if ext else ""
