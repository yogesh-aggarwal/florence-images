import os
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin SDK
cert = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cert)


# Upload a single file to Firebase Storage
def upload_file_to_firebase(local_file_path, firebase_folder):
    bucket = storage.bucket()

    filename = os.path.basename(local_file_path)
    blob = bucket.blob(f"{firebase_folder}/{filename}")
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded {filename} to Firebase Storage in folder {firebase_folder}")


# Ensure the Firebase folder exists (Firebase Storage is flat, so we just use the folder name as a prefix)
def upload_files_to_firebase(local_folder, firebase_folder):
    files = os.listdir(local_folder)
    files = tuple(
        filter(lambda x: os.path.isfile(os.path.join(local_folder, x)), files)
    )
    if not files:
        print(f"No files found in {local_folder}")
        return

    for filename in os.listdir(local_folder):
        local_file_path = os.path.join(local_folder, filename)
        upload_file_to_firebase(local_file_path, firebase_folder)


def main():
    local_folder = "./images"
    firebase_folder = "/images/products"
    upload_files_to_firebase(local_folder, firebase_folder)
