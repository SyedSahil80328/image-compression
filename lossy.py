from PIL import Image
import os

def compress_image(input_path, output_path, quality=50):
    """
    Compress an image to reduce its file size.

    Parameters:
    input_path (str): Path to the input image file.
    output_path (str): Path to save the compressed image.
    quality (int): Quality level for the compressed image (1 to 100, where 100 is the best quality).
    """
    try:
        # Open the image file
        img = Image.open(input_path)

        # Compress and save the image
        img.save(output_path, optimize=True, quality=quality)
        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error compressing image: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "input.jpg"
    output_image_path = "lossy_output.jpg"

    # Ensure the output directory exists
    # os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    compress_image(input_image_path, output_image_path, quality=30)