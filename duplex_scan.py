from pypdf import  PdfReader, PdfWriter
import math
import os


#------------------------ Path -----------------------
def get_file_path():
    while True:
        path = input("Bitte gib den vollständigen Pfad zu einer Datei ein: ").strip()

        if os.path.isfile(path):
            print(f"Datei gefunden: {path}")
            return path
        else:
            print("Datei nicht gefunden. Bitte versuche es erneut.\n")
path = get_file_path()



#------------------- Reading --------------
reader = PdfReader(path)
writer = PdfWriter()
number_of_pages = len(reader.pages)



#--------------- Sorting ---------------
i = 0
j = number_of_pages - 1

while i < j:
    writer.add_page(reader.pages[i])
    writer.add_page(reader.pages[j])
    i = i+1
    j = j-1

if i == j and number_of_pages % 2 != 0:
    writer.add_page(reader.pages[i])

#-------------- Writing ----------------
new_filename =  os.path.join(os.path.dirname(path), "sorted_" + os.path.basename(path))
with open(new_filename, "wb") as f:
    writer.write(f)

print(" Wurde erfolgreich nach  \n" + new_filename + "\n" + "geschrieben."  )
