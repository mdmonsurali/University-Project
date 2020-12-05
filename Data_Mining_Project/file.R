
#Used library function

library(tidyverse)
library(dplyr)
library(ggplot2)


#Loading both dataset from desktop

file1= read.csv("C:/Users/proth/Desktop/Data Mining/meter_readings_export_homework.csv")
 View(file1)

file2 =  read.csv("C:/Users/proth/Desktop/Data Mining/metering_points_homework.csv")
 View(file2)

#Merged both dataset by pod_id and order dataset by pod_id and ACTUAL_DATE_OF_METER_READING
 
file3 <- merged.data <- merge(file1, file2, by="pod_id")
 View(file3)

file3 <- file3[order(file3$pod_id, file3$ACTUAL_DATE_OF_METER_READING) , ]
View(file3)

#Rename dataset

file3 <- select(file3,podid=pod_id, date=ACTUAL_DATE_OF_METER_READING, billedreading=BILLED_METER_READING,mrtype=METER_READING_TYPE,mrcategory=METER_READING_CATEGORY,country=pod_country,postalcode=pod_postal_code,city=pod_city,LONG,LAT)
View(file3)

#Used Lag for making bill reading difference and date deference and used mutate for adding new coloum

file4<-mutate(file3,LAGbilledreading=lag(billedreading),LAGdate=lag(date))
View(file4)


file5<-mutate(file4,energyconsumption=as.numeric(as.character(billedreading))-as.numeric(as.character(LAGbilledreading)),dateofconsumption=as.numeric(as.Date((date)),format="%d-%m-%y")-as.numeric(as.Date((LAGdate)),format="%d-%m-%y"))
View(file5)

#Create new coloum for yearly consumtion 




file6<-mutate(file5,yearlyconsum=round(energyconsumption*365/as.numeric(dateofconsumption)))

View(file6) 

#Remove null rows

finaldataset<-na.omit(file6)
View(finaldataset)

#Used K-means Clustering(4) for Question - a

results <- kmeans(finaldataset[9:10],4,20)

results

table(finaldataset$city,results$cluster)

#Used ggplot for visualizing region differences

ggplot(data = finaldataset, aes(x=LAT, y=LONG, colour=results$cluster)) + geom_point(size=1.5)




#Question2

#Used mutate for adding all cluster according to k-means algorithm

finaldataset<-mutate(finaldataset,regioncluster=results$cluster)
View(finaldataset)

final=finaldataset
View(final)

#Re-format the date and used subset and separate 2015 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

A=subset(final, LAGdate> "2015-01-01" & LAGdate < "2015-12-31")

View(A)

#Used boxplot chart for visualize regional differencec in 2015

boxplot(yearlyconsum~regioncluster,data=A,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2015 - Energy consumption(kwh)",main="2015 - Energy consumption of 4 differernt region")




#Question3



#2010
#Re-format the date and used subset and separate 2010 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2010=subset(final, LAGdate> "2010-01-01" & LAGdate < "2010-12-31")

View(consum2010)

boxplot(yearlyconsum~regioncluster,data=consum2010,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2010 - Energy consumption(kwh)",main="2010 - Energy consumption of 4 differernt region")



#2011
#Re-format the date and used subset and separate 2011 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2011=subset(final, LAGdate> "2011-01-01" & LAGdate < "2011-12-31")

View(consum2011)


boxplot(yearlyconsum~regioncluster,data=consum2011,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2011 - Energy consumption(kwh)",main="2011 Energy consumption of 4 differernt region")


#2012
#Re-format the date and used subset and separate 2012 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2012=subset(final, LAGdate> "2012-01-01" & LAGdate < "2012-12-31")

View(consum2012)

boxplot(yearlyconsum~regioncluster,data=consum2012,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2012 - Energy consumption(kwh)",main="2012 - energy consumption of 4 differernt region")


#2013
#Re-format the date and used subset and separate 2013 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2013=subset(final, LAGdate> "2013-01-01" & LAGdate < "2013-12-31")

View(consum2013)


boxplot(yearlyconsum~regioncluster,data=consum2013,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2013 - Energy consumption(kwh)",main="2013 - energy consumption of 4 differernt region")


#2014
#Re-format the date and used subset and separate 2014 years dataset

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2014=subset(final, LAGdate> "2014-01-01" & LAGdate < "2014-12-31")

View(consum2014)

boxplot(yearlyconsum~regioncluster,data=consum2014,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2014 - Energy consumption(kwh)",main="2014 - energy consumption of 4 differernt region")



#2015
#Re-format the date and used subset and separate 2015 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2015=subset(final, LAGdate> "2015-01-01" & LAGdate < "2015-12-31")

View(consum2015)

boxplot(yearlyconsum~regioncluster,data=consum2015,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2015 - Energy consumption(kwh)",main="2015 - energy consumption of 4 differernt region")


#2016
#Re-format the date and used subset and separate 2016 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2016=subset(final, LAGdate> "2016-01-01" & LAGdate < "2016-12-31")

View(consum2016)

boxplot(yearlyconsum~regioncluster,data=consum2016,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2016 - Energy consumption(kwh)",main="2016 - energy consumption of 4 differernt region")


#2017
#Re-format the date and used subset and separate 2017 years dataset 

final$LAGdate <- as.Date(final$LAGdate, format= "%Y-%m-%d")

consum2017=subset(final, LAGdate> "2017-01-01" & LAGdate < "2017-12-31")

View(consum2017)

boxplot(yearlyconsum~regioncluster,data=consum2017,col=c("gray70","purple1","olivedrab2","turquoise2"),xlab="Region (cluster groups)",ylab="2017 - Energy consumption(kwh)",main="2017 - energy consumption of 4 differernt region")


