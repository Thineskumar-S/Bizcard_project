import easyocr as ocr
from PIL import Image
import numpy as np

# calling ocr neural network for english language
reader=ocr.Reader(['en'])


def extract_text(img_path):
    img=Image.open(img_path)
    img_array=np.array(img) 
    result = reader.readtext(img_array, detail = 0)
    result1= reader.readtext(img_array, detail = 0,paragraph=True)
    return result,result1