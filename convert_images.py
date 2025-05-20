from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# List of SVG files to convert
svg_files = [
    'logo.svg',
    'himalayas.svg',
    'team-photo.svg',
    'opponent-logo.svg',
    'gallery1.svg',
    'gallery2.svg',
    'gallery3.svg'
]

# Convert each SVG to PNG
for svg_file in svg_files:
    input_path = os.path.join('images', svg_file)
    output_path = os.path.join('images', svg_file.replace('.svg', '.png'))
    
    # Convert SVG to PNG
    drawing = svg2rlg(input_path)
    renderPM.drawToFile(drawing, output_path, fmt='PNG')
    
    print(f'Converted {svg_file} to PNG') 