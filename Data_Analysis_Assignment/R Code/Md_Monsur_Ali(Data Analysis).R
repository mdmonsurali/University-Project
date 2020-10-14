library(sqldf)
library(dplyr)
library(tidyverse)
library(dplyr)
library(ggplot2)

#Md Monsur Ali
#Matriculation No: 24547
#Data Analysis and Statistics  

#Modelling a single female without a calf and Modelling a single female with a calf: :

#Ques:16
recruits <- c()
ages<- c()

#Ques:17
#Simulate 1000 female life histories
for (i in 1:1000){     

#Define all variables  
#Ques:1
co<-rnorm(1,100,10)

#Ques:2
age<- 15

#Ques:3
alive <- 1

#Ques:4
enMu<- 0
enSD<- 20

#------------Ques 18-24  ------------#

# #Scenario 1: Rich and stable environment
# enMu<- 20
# enSD<- 1

# #Scenario 2: Poor and stable environment
# enMu<- 2
# enSD<- 1
# 
# #Scenario 3: Rich and variable environment
# enMu<- 20
# enSD<- 30
# 
# #Scenario 4: Poor and variable environment
# enMu<- 2
# enSD<- 30

#------------Ques 18-24  ------------#

#Ques:5
sr<-0.8

#Ques:6
s0<- -2
s1<- 0.05

#Ques:10
calf <- 0
calfage <- 0
offspring <- 0

#Ques:12
b0 <- -10
b1 <- 0.1

#Ques:13
inv <- 10
recruit <- 0
calfborn <- c()


#Ques:7
while (alive>0 && age<=40 ) {
  
  #Ques:9
  sr <- exp(s0 + s1 * co)/(1 + exp(s0 + s1 * co))
  if (rbinom(1, 1, sr) == 1) { 
    
    #Modelling a single female with a calf:
    #female doesn't have a calf,
    #Ques:14
    if (calf == 0) {
      b <- exp(b0 + b1 * co)/(1 + exp(b0 + b1 * co))
      if (rbinom(1, 1, b) == 1 ) {
        
        #calf is born
        calf <- 1
        
      }
    } else {
      
      #female has a calf
      co <- co - inv
      if (rbinom(1, 1, 0.8) == 1) {
        #calf is going to surviv
        calfage <- calfage + 1
        
      } else {
        
        #calf has died
        calf <- 0
        calfage <- 0
      }
      #15 independence reached
      if (calfage > 4) {
        offspring <- offspring + 1
        calfborn <- cbind(calfborn,age)
        calf <- 0
        calfage <- 0
      }
    }
    age <- age + 1
    co <- co + rnorm(1, enMu, enSD)
  } else {
    
    # female is dead
    alive <- 0
  }
}

if (length(calfborn)>0){
  for (j in 1:length(calfborn)){
    if ((age-calfborn[[j]]-5)>=15 && rbinom(1,1,0.98)){
      recruit <- recruit + 1
    }
  }
  
}


ages <- cbind(ages,age)
recruits <- cbind(recruits,recruit)
avgrecruits <- mean(recruits)
}

# Visualizing results

#Ques:19
hist(ages, main = "Female Ages at the end of reproduction", xlab = "Ages", border="brown", col="black")

#Ques:20
hist(recruits, main = "Female as its Inclusive fitness", xlab = "Recruits", border="brown", col="black")

#Ques:21
avgrecruits
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    



