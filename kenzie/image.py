from flask import request, safe_join, jsonify
from flask.helpers import send_from_directory
from werkzeug.utils import secure_filename
import os
from environs import Env
from os import environ
from zipfile import ZipFile


env = Env()
env.read_env()

FILES_DIRECTORY = environ.get('FILES_DIRECTORY')
MAX_CONTENT_LENGTH = int(environ.get('MAX_CONTENT_LENGTH'))


def save_file() -> bool:
    """Capture files from request.files, name them using secure_filename, save in a specific folder."""

    len_file = int(request.headers["Content-Length"])
    files_list = list(request.files)

    if len(files_list) <= 0 | len_file > MAX_CONTENT_LENGTH:
        return False

    for f in files_list:
        received_file = request.files[f]

        filename = secure_filename(received_file.filename)

        file_path = safe_join(f"{FILES_DIRECTORY}/{filename.split('.')[-1].upper()}", filename)

        files = os.listdir(f"{FILES_DIRECTORY}/{filename.split('.')[-1].upper()}")

        if filename in files:

            return "existing file"

        received_file.save(file_path)

    return True


def get_files():
    """Searches all files within a specified folder and returns a list of all of them. If the folder is empty it returns False."""

    files = os.listdir(FILES_DIRECTORY)
    all_files = []

    for file in files:
        file = os.listdir(f"{FILES_DIRECTORY}/{file}")
        if len(file) >= 1:
            all_files.append(file)

    if len(all_files) == 0:
        return False

    return jsonify(all_files)


def get_type_files(type: str):
    """Searches all files of a specified extension in a specified folder and returns a list of all of them. If the folder is empty, it returns False."""

    files = os.listdir(f"{FILES_DIRECTORY}/{type.upper()}")

    if len(files) <= 0:
        return False

    return files


def download_zip():
    """
    It captures the file type and compression level, creates a Zip file and returns the file for download.
    """

    file_type = request.args.get("file_type")
    compression_rate = int(request.args.get("compression_rate"))
    files = os.listdir(f"{FILES_DIRECTORY}/{file_type.upper()}")

    with ZipFile(f'./ZIP/zip_{file_type.upper()}.zip', 'w', compresslevel=compression_rate) as myzip:
        for i in files:
            myzip.write(f'./upload/{file_type.upper()}/{i}')

    return send_from_directory("../ZIP", f'zip_{file_type.upper()}.zip', as_attachment=True)
