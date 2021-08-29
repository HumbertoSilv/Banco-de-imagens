import os

UPLOAD_DITECTORY = "./upload"

if not os.path.exists(UPLOAD_DITECTORY):
    os.makedirs(UPLOAD_DITECTORY)
    os.makedirs(f"{UPLOAD_DITECTORY}/GIF")
    os.makedirs(f"{UPLOAD_DITECTORY}/JPG")
    os.makedirs(f"{UPLOAD_DITECTORY}/PNG")
