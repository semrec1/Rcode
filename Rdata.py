#b. Reading and Writing of different types of data sets  
#i. Reading  different  types  of  datasets (.txt,csv) from web and disk and writing in file in specific disk location.
#ii. Reading Excel datasheet in R.
#iii. Reading XML dataset in R.

#i.Reading  different  types  of  datasets (.txt,csv) from web and disk and writing in file in specific disk location.
library(utils)
library(datasets)
data<-read.csv("data.csv")
data
# get all employees in IT
frame.data=read.csv("data.csv")
retval=subset(data,dept =="IT")

retval
 #write into new file
write.csv(retval,"output.csv")
newdata=read.csv("output.csv")
newdata

# ii .reading excel datasheet
install.packages("xlsx")
library(xlsx)
data= read.xlsx("data.xlsx",sheetIndex = 1)
data

# iii.reading XML in R
install.packages("XML")
library("XML")
library("methods")
result= xmlParse(file="input.xml")
result
