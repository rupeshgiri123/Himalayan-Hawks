from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Convert SVG to PNG
drawing = svg2rlg('images/logo.svg')
renderPM.drawToFile(drawing, 'images/logo.png', fmt='PNG') 