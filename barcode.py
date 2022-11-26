from pyzbar import pyzbar
import cv2
import sys
from glob import glob

def decode(image):
    
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print(obj.data)
    return image
    
if __name__ == "__main__":
    
    img = cv2.imread(sys.argv[1])
    img = decode(img)
    
    
#    barcodes = sorted(glob("*.png"))
#    for barcode_file in barcodes:
#        img = cv2.imread(barcode_file)
#        img = decode(img)
        
        
