# Python3 program to convert image to pfd 
# using img2pdf library 

# importing necessary libraries 
import img2pdf 
from PIL import Image 
import os 

# Importing Required Module
# Creating Image File Object
ImgFile = open("test1.jpg","rb")
# Creating PDF File Object
PdfFile = open("test1.pdf","wb")
# Converting Image File to PDF
PdfFile.write(img2pdf.convert(ImgFile))
#Closing Image File Object
ImgFile.close()
#Closing PDF File Object
PdfFile.close()