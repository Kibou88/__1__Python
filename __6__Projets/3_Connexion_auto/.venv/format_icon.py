from PIL import Image

def convert_png_to_ico(png_path, ico_path, size=(256, 256)):
    # Open the PNG image
    img = Image.open(png_path)

    # Resize the image to the desired size (optional, but ICO files typically require specific sizes)
    img = img.resize(size, Image.LANCZOS)

    # Save the image in ICO format
    img.save(ico_path, format='ICO')

# Example usage
png_path = '.\\datas\\icone_server.png'  # Replace with the path to your PNG file
ico_path = '.\\datas\\icone_server.ico'  # Replace with the desired path for the ICO file
convert_png_to_ico(png_path, ico_path)