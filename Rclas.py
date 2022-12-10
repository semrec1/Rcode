#b. Create a classification model 
#i Install relevant package for classification. 
#ii. Choose classifier for classification problem. 
#iii. Evaluate the performance of classifier.

# i Install relevant package for classification. 
install.packages("rpart.plot")
install.packages("tree")
install.packages("ISLR")
install.packages("rattle")

library(tree)
library(ISLR)
library(rpart.plot)
library(rattle)


#ii. Choose classifier for classification problem. 

attach(Hitters)
View(Hitters)
#remove NA data
Hitters= na.omit(Hitters)


Hitters$Salary<-log(Hitters$Salary)
hist(Hitters$Salary)
