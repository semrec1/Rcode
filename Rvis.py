# b. Visualizations 
#       i. Find the data distributions using box and scatter plot.
#       ii. Find the outliers using plot.
#       iii. Plot the histogram, bar chart and pie chart on sample data.

# i.Find the data distributions using box and scatter plot.
#find the data distribution using box and scatter plot
install.packages("ggplot2")
library(ggplot2)
library(datasets)
input= mtcars[,c('mpg','cyl')]
input
boxplot(mpg~cyl,data = mtcars,xlab="number of cyl",ylab = "miles per gallon",main = "mileage data") #boxplot
plot(input) #scatter plot
dev.off()

# ii.find outliers using plot
v=c(50,75,100,125,150,175,200)
boxplot(v)

# iii.Plot the histogram barchart and piechart on sampledata
library(graphics)
v=c(9,13,21,8,36,22,12,41,31,33,19)
# creating histogram
hist(v,xlab = "weight",col="blue",border = "green")

# barchart
h=c(7,12,28,3,41)
m=c("jan","feb","march","april","may")
barplot(h,names.arg=m,xlab="month",ylab="revenue",col="blue",main="revenuechart",border="orange")

# piechart
x=c(21,62,10,53)
labels=c("london","new york","singapore","mumbai")
pie(x,labels)
