from PIL import Image, ImageDraw, ImageOps
import os

ASSETS_DIR = "./assets"
INPUT_DIR = os.path.join(ASSETS_DIR, "pre-processing")
OUTPUT_DIR = os.path.join(ASSETS_DIR, "post-processing")
RADIUS = 20

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def round_image(filename):
    path = os.path.join(INPUT_DIR, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    # Open image and convert to RGBA
    img = Image.open(path).convert("RGBA")
    
    # Supersampling factor for anti-aliasing
    factor = 4
    
    # Create high-res mask
    mask = Image.new('L', (img.size[0] * factor, img.size[1] * factor), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw rounded rectangle on high-res mask
    draw.rounded_rectangle(
        [(0, 0), (img.size[0] * factor, img.size[1] * factor)], 
        radius=RADIUS * factor, 
        fill=255
    )
    
    # Resize mask down with high-quality resampling (LANCZOS)
    mask = mask.resize(img.size, Image.Resampling.LANCZOS)
    
    # Apply mask
    output = img.copy()
    output.putalpha(mask)
    
    # Save as new file in OUTPUT_DIR
    new_filename = filename.replace(".png", "-rounded.png")
    output_path = os.path.join(OUTPUT_DIR, new_filename)
    output.save(output_path)
    print(f"Saved: {output_path}")

# Process all PNG files in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".png"):
        print(f"Processing: {filename}")
        round_image(filename)
