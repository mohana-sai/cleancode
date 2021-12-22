
#importing essential library
import camelot
#read the file
pdf = camelot.read_pdf("structured.pdf", pages='all')
#type of pdf
print(type(pdf))
#knowing the table list
print(pdf)
#knowing the table shape
print(pdf[1])
#Assinging variable to a pdf file
structured_pdf = pdf[1]
print(structured_pdf.df)
#Converting to csv file
structured_pdf.to_csv("structured.csv")
print(pdf[1].parsing_report) #knowing the accuracy
