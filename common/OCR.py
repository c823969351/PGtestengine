from matplotlib import image
import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\mega\Desktop\ocrtest.jpg')
code = pytesseract.image_to_string(image,lang='eng')
print(code)