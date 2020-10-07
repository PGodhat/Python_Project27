#import libraries
import cv2
import pytesseract
from PIL import Image
import sys
import os
from pdf2image import convert_from_path as getImgsFromPDF
pytesseract.pytesseract.tesseract_cmd='C:\\Users\\SHIVAM\\Tesseract-OCR\\tesseract.exe'


path=input('Please enter the complete path of the pdf:\n')  #input path of pdf
pages = getImgsFromPDF(pdf_path = path,dpi = 200,size = (1654,2340),poppler_path='C:\\Users\\SHIVAM\\poppler-0.68.0\\bin')   # store all the pages of the pdf in a variable
page_no=1
for page in pages:    #go through all the pages stored in pages 
    name="page_"+str(page_no)+".jpg"
    page.save(name,'JPEG')   # Save the image of the page in system
    page_no+=1
    
for i in range(1,page_no):       # Iterate through all the pages
    img_path="page_"+str(i)+".jpg"
    print('*****************************************************Page - ',i,'*****************************************************')
    img=cv2.imread(img_path)  #read image
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #Converting BGR to RGB because pytesseract accepts only RGB but in opencv it's BGR
    print(pytesseract.image_to_string(img))
