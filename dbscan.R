#DB Scan for 2 class classification or anomaly detection
file = read.csv("C:\\Pgdba\\assignments\\FADML\\assignment_2\\HPC-job-failure-prediction-assignment-master\\train_data.csv")
library(dbscan)
db = dbscan(file[,1:4], eps = 0.8, minPts = 4)
ind = vector()

for(i in 1:length(db$cluster)){
  if(db$cluster[i] == 0){
    ind = append(ind, i)
  }
}

#There are more than one clusters. And 0 is the outlier. 
#Labelling other clusters as 1
db$cluster[db$cluster != 0] = 1

failed = file[,5]    #for easy operations labels are taken in a variable
#outliers in our file is labeled 1. And our db scan models outliers as 1
#Thus we tweak our file labels
failed[failed == 0] = 2
failed[failed == 1] = 0
failed[failed == 2] = 1

accuracy = 1 - sum(abs(db$cluster - failed))/20000
print(accuracy)