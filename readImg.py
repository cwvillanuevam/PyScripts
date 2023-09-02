import pytesseract
from PIL import Image

# Cargar la imagen
imagen = Image.open('AEEs.png')

# Aplicar OCR a la imagen
texto_extraido = pytesseract.image_to_string(imagen)

# Imprimir el texto extraído
print(texto_extraido)
