# apt-get update && apt-get install libgl1 (instalar no sistema)
# (instalar no sistema) - sudo apt-get install python3-pil tesseract-ocr libtesseract-dev tesseract-ocr-eng tesseract-ocr-script-latn

import cv2
import pytesseract

# Carrega a imagem em escala de cinza
img = cv2.imread('imei2.jpg', cv2.IMREAD_GRAYSCALE)
# Extrai o texto da imagem
texto = pytesseract.image_to_string(img)

# Imprime o texto extraído
print(texto)
print(texto.split())