import os

def delete_all(base_directory):
    for image in os.listdir(base_directory):
        image_path = os.path.join(base_directory, image)
        if os.path.isfile(image_path):
            os.remove(image_path)

if __name__ == "__main__":
    base_directory = "C:/Passdown-SnapShot/Clipboard_Images"
    delete_all(base_directory)