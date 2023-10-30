# Importar las librerías necesarias
import PyPDF2
import re
 
# Abrir el archivo PDF en modo binario
pdf_file = open('/mnt/c/Users/jormonto/Documents/Proyecto IA - Los Meros/content/output_papers/certificadolibertadytradicion.pdf', 'rb')
 
 
# Crear un objeto lector de PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
 
print(pdf_reader)
# Obtener el número de páginas del PDF
num_pages = len(pdf_reader.pages)
 
print(pdf_reader.pages)
 
print(f'El PDF tiene {num_pages} páginas')
 
 
page_obj = pdf_reader.pages[0]
 
page_text = page_obj.extract_text()
 
def extract_text (page_tex):
 
    pattern = re.findall(r'ESPECIFICACION:.*:.*',page_tex)
    print(pattern)
    return pattern
 
# Extraer el texto de la página
 
 
extract_text(page_text)
 
# Imprimir las posiciones donde se encuentra la palabra clave
#for match in matches:
#    print(f'La palabra {keyword} se encuentra en la posición {match.start()}')
 
 
# Cerrar el archivo PDF
pdf_file.close()
