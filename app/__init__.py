from kenzie.image import download_zip, get_files, get_type_files, save_file
from flask import Flask, jsonify
from flask.helpers import send_from_directory
from environs import Env
import os

env = Env()
env.read_env()

app = Flask(__name__)


@app.post("/upload")
def upload():
    mock = save_file()
    try:
        if not mock:
            return jsonify({"msg": "No file uploadded"}), 413

        elif mock == "existing file":
            return jsonify({"msg": "FAILED : existing file"}), 409

    except FileNotFoundError:
        return jsonify({"msg": "FAILED : unsupported file type"}), 415

    return jsonify({"msg": "Upload success"}), 201


@app.get("/files")
def list_files():
    if not get_files():
        return jsonify({"msg": "No files"}), 400

    return get_files(), 200


@app.get("/files/<type>")
def list_files_by_type(type):
    try:
        if not get_type_files(type):
            return jsonify({"msg": "Files not found"}), 404

    except FileNotFoundError:
        return jsonify({"msg": "FAILED : unsupported file type"}), 415

    return jsonify(get_type_files(type)), 200


@app.get("/download/<file_name>")
def download(file_name):
    files = os.listdir(f"./upload/{file_name[-3:].upper()}")

    try:
        if not (file_name in files):
            return jsonify({"msg": "filename not found"}), 404

    except FileNotFoundError:
        return jsonify({"msg": "filename not found"}), 404

    return send_from_directory(directory=f"../upload/{file_name[-3:].upper()}",
                               path=file_name, as_attachment=True)


@app.get("/download-zip")
def download_dir_as_zip():
    try:
        return download_zip()

    except TypeError:
        return jsonify({"msg": "Incorrect arguments, check them out."}), 404
