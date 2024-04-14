import os
from django.conf import settings

def handle_uploaded_image(uploaded_file):
    # Define the directory where uploaded images will be saved
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')

    # Create the directory if it doesn't exist
    os.makedirs(upload_dir, exist_ok=True)

    # Generate a unique file name for the uploaded image
    file_name = uploaded_file.name

    # Write the uploaded image to the disk
    file_path = os.path.join(upload_dir, file_name)
    with open(file_path, 'wb') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)

    # Return the path to the uploaded image
    return file_path
