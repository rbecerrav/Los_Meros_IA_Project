from ctypes.util import find_library
import os
import ocrmypdf as ocrmypdf
 
 
find_library("gs")
 
 
file_list = []
 
input_folder_path = "/mnt/c/Users/jormonto/Documents/Proyecto IA - Los Meros/content/input_papers"
output_folder_path = "/mnt/c/Users/jormonto/Documents/Proyecto IA - Los Meros/content/output_papers"
 
for filename in os.listdir(input_folder_path):
    if filename.endswith("pdf"):
      file_list.append(filename)
 
print("The following files will be converted : ")
 
 
for filename in file_list:
  print("Converting : " + filename)
  input_filename = input_folder_path+'/'+filename
  output_filename = output_folder_path+'/'+filename
 
  ocrmypdf.ocr(input_filename, output_filename, skip_text=True)
