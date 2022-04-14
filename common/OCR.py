from matplotlib import image
import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\mega\Desktop\ocrtest1.jpg')
code = pytesseract.image_to_string(image,lang='chi_sim')
print(code)