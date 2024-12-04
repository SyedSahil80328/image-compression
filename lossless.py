from PIL import Image
import gzip

def compress_image_lossless(input_path, output_path):
    """
    Compress an image to reduce its file size without losing quality.
    
    Parameters:
    input_path (str): Path to the input image file.
    output_path (str): Path to save the compressed image.
    """
    try:
        # Open the image file
        img = Image.open(input_path)

        # Save the image in PNG format (lossless compression)
        img.save(output_path, format='PNG', compress_level=9)
        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error compressing image: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "input.jpg"  # Change this to your image file
    output_image_path = "lossless_output.png"  # Ensure it's a .png or other lossless format

    # Ensure the output directory exists
    # os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    compress_image_lossless(input_image_path, output_image_path)

    with open("lossless_output.png", "rb") as f_in:
        with gzip.open("compressed_output.gz", "wb") as f_out:
            f_out.writelines(f_in)