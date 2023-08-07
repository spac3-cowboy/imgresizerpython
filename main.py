from PIL import Image
import os

def resize_images(input_dir, output_dir, new_size):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            img = Image.open(image_path)
            img = img.resize(new_size, Image.LANCZOS) 
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
            print(f"Resized {filename}")

if __name__ == "__main__":
    input_directory = os.path.dirname(os.path.abspath(__file__))  # Use the script's directory as input
    output_directory = os.path.join(input_directory, "new")  # Create a 'new' directory in the script's directory
    new_image_size = (800, 600)  # Replace with your desired image size (width, height)

    resize_images(input_directory, output_directory, new_image_size)
    print("Done")