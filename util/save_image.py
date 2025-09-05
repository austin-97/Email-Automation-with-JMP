import os
from PIL import ImageGrab
from datetime import datetime

def save_clipboard_image_to_dir(base_directory, filename, file_extension=".png"):

    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    counter = 0
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file_path = os.path.join(base_directory, f"{filename}-{counter}-{timestamp}{file_extension}")

    while os.path.exists(output_file_path):
        counter += 1
        output_file_path = os.path.join(base_directory, f"{filename}-{counter}-{timestamp}{file_extension}")

    image = ImageGrab.grabclipboard()

    if image is None:
        print("No image found in the clipboard.")
        return

    try:
        image.save(output_file_path, "PNG")
        print(f"Image saved to {output_file_path}")
    except Exception as e:
        print(f"Failed to save image: {e}")

if __name__ == "__main__":
    base_directory = r"C:\Passdown-SnapShot\Clipboard_Images"
    filename = "report"
    save_clipboard_image_to_dir(base_directory, filename)