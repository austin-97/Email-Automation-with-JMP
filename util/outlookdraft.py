import win32com.client
import os
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def create_outlook_draft_with_images(base_directory):

    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    
    mail.Subject = "JMP Email Automation Examples"
    hyperlink = '<a href="https://github.com/austin-97">Github/austin-97</a>'
    body = f'Good Morning,<br><br>This is JMP! and a bit of python<br><br>{hyperlink}<br><br>'

    png_files = sorted([f for f in os.listdir(base_directory) if f.endswith('.png')])
    for image in png_files:
        if image.endswith('.png'):
            image_path = os.path.join(base_directory, image)
            body += f'<img src="data:image/jpeg;base64,{image_to_base64(image_path)}" alt="Embedded Image"/><br>'
    
    body += "<br><br> Best, <br>JMP!"
    mail.HTMLBody = body
    mail.Save()

    print("Draft email with images created successfully!")

if __name__ == "__main__":
    base_directory = "C:/Passdown-SnapShot/Clipboard_Images"
    create_outlook_draft_with_images(base_directory)