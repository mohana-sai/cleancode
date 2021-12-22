
#importing essential library
import camelot
#read the file
pdf = camelot.read_pdf("semistructured.pdf", pages='all')
#type of pdf
print(type(pdf))
#knowing the table list
print(pdf)
#knowing the table shape
print(pdf[1])
#Assinging variable to a pdf file
semistructured_pdf = pdf[1]
print(semistructured_pdf.df)
#Converting to csv file
semistructured_pdf.to_csv("semistructured.csv")
print(pdf[1].parsing_report) #knowing the accuracy
