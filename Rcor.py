#    b. Correlation and Covariance 
#        i. Find the correlation matrix.
#        ii. Plot the correlation plot on dataset and 
#            visualize giving an overview of relationships among data on iris data.

# find correlation matrix and visualize giving an overview of relationships among data on iris data.

install.packages("DataExplorer")
install.packages("corrplot")
library(ggplot2)
library(tidyr)
library(datasets)
library(DataExplorer)
library(corrplot)
data("iris")
title="matrix_iris"
plot_correlation(iris)
seto<-iris[iris$Species =='setosa',c("Sepal.Length","Petal.Length","Species")]
ggplot(seto)+
  geom_point(mapping=aes(x=seto$Sepal.Length,y=seto$Petal.Length),position = "jitter")+
  ggtitle("Sepal Length vs. Petal Length-Jitter scatter plot")
