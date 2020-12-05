library(tidyverse)
library(dplyr)
library(ggplot2)



# Task 'A' [To evaluate the Regional Differences]

#Datasets of metering_points from excel file
metering_points_homework=read.csv("C:/Users/proth/Desktop/Data Mining/metering_points_homework.csv")
View(metering_points_homework)
selectedDataOf_metering_points_homework= select ( metering_points_homework,LONG=LONG,LAT=LAT)

# Use of K-Means
geoLocationCluster=kmeans(selectedDataOf_metering_points_homework,4) 
Regions=geoLocationCluster$cluster
View(Regions)
table(metering_points_homework$pod_city,geoLocationCluster$cluster)

#Use of ggplot to visualize the data
ggplot(data = selectedDataOf_metering_points_homework,
       aes( x = LAT, y = LONG,
            color = Regions)) + geom_point() +
  theme( legend.position="left")



#Task 'B'[Comparison of Energy Consumption to different regions]

#Datasets of meter_readings from excel file 
meter_readings_expert_homework=read.csv("C:/Users/proth/Desktop/Data Mining/meter_readings_export_homework.csv")
p= select ( meter_readings_expert_homework,PODID=pod_id,reading=BILLED_METER_READING,date=ACTUAL_DATE_OF_METER_READING)
q=arrange(p,PODID,as.Date(date,format="%d/%m/%Y"))
q$date=as.Date(q$date,format="%m/%d/%Y")
q = q[order(q$PODID, q$date),]

#lag
r=group_by(q,PODID) %>%mutate(prevread=lag(reading),prevdate=lag(date)) 

#get dateDifferences and reading Differences
r$dateDiff=r$date-r$prevdate 
View(s)
r$readingDiff=as.numeric(r$reading-r$prevread)

s= select ( metering_points_homework,PODID=pod_id,LONG=LONG,LAT=LAT,City=pod_city)%>%mutate(clusterType=geoLocationCluster$cluster)

joinedTable=left_join(r,s,by="PODID")

removeNa = joinedTable[, 6:7][is.na(joinedTable[, 6:7])] <- 0

joinedTable <- joinedTable[ which( joinedTable$dateDiff !=0 & joinedTable$readingDiff !=0) , ]

joinedTable <- joinedTable[,colSums(is.na(joinedTable))<nrow(joinedTable)]
View(joinedTable)

EachYearConsumptionAvg=as.double(joinedTable$readingDiff)/as.double(joinedTable$dateDiff)  * 365
joinedTable$EachYearConsumptionAvg=EachYearConsumptionAvg



#2015
energyConsumttion_2015=subset(joinedTable,format(as.Date(prevdate),"%Y")==2015)
boxplot(EachYearConsumptionAvg~clusterType,data=energyConsumttion_2015,col=c("green","pink","grey","red"))

# 3rd question

#Cluster 1
install.packages("lubridate")
library(lubridate)
getTheDataForClusterOne=subset(joinedTable,clusterType==1) 
boxplot(EachYearConsumptionAvg~year(prevdate),data=getTheDataForClusterOne,col=c("yellow","green","blue","red","purple","orange","gray","pink"))


#Cluster 2
getTheDataForClusterTwo=subset(joinedTable,clusterType==2) 
boxplot(EachYearConsumptionAvg~year(prevdate),data=getTheDataForClusterTwo,col=c("yellow","green","blue","red","purple","orange","gray","pink"),main="cluster 1")


#Cluster 2
getTheDataForClusterTwo=subset(joinedTable,clusterType==2) 
boxplot(EachYearConsumptionAvg~year(prevdate),data=getTheDataForClusterTwo,col=c("yellow","green","blue","red","purple","orange","gray","pink"),main="cluster 2")

#Cluster 3
getTheDataForClusterThree=subset(joinedTable,clusterType==3) 
boxplot(EachYearConsumptionAvg~year(prevdate),data=getTheDataForClusterThree,col=c("yellow","green","blue","red","purple","orange","gray","pink"),main="cluster 3")

#Cluster 4
getTheDataForClusterFour=subset(joinedTable,clusterType==4) 
boxplot(EachYearConsumptionAvg~year(prevdate),data=getTheDataForClusterFour,col=c("yellow","green","blue","red","purple","orange","gray","pink"),main="cluster 4")