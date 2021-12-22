#importing essential library
import camelot
#reading the file
pdf = camelot.read_pdf("unstructured.pdf", pages='all')
#knowing the type of pdf
print(type(pdf))
#knowing the table list
print(pdf)
#we cannot extract data which is not in tabular format
print(pdf[1])
