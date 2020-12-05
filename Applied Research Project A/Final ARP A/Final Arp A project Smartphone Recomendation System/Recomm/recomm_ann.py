# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:59:35 2019

@author: Sudarshan
"""

#importing libraries
import pandas as pnd
import numpy as nmp
from encodinginputvars import InputEncoders
from morerecommendations import MoreRecommendations
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense

#removing the warnings 
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class RecommendationSystem:
    
    system_trained = False
        
    input_encoder = InputEncoders()
    recommend_more = MoreRecommendations()

    #importing the dataset
    dataset = pnd.read_csv('data_survey_final_1.csv') #please provide the proper directory while testing

    #independent variable matrix
    X = dataset.iloc[:,0:14]
    #dependent variable
    y = dataset.iloc[:,14]

    X = pnd.get_dummies(X,drop_first=True)

    y = pnd.get_dummies(y,drop_first=True)

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.01 ,random_state = 0)

    classifier = Sequential() 
    
    #function to train the recommendation system
    def TrainRecommendationSystem(self):
        #Adding input layer and ist hidden layer
        self.classifier.add(Dense(output_dim = 45,init = 'uniform', activation= 'relu',input_dim = 28))
        #2nd hidden layer
        self.classifier.add(Dense(output_dim = 45,init = 'uniform', activation= 'relu'))
        #adding the output layer
        self.classifier.add(Dense(output_dim = 63,init = 'uniform', activation= 'softmax'))
        #compiling ANN
        self.classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) 
        #training 
        self.classifier.fit(self.X_train,self.y_train,batch_size = 10, epochs = 100)
        self.system_trained = True
        print('Training complete')
        
        #function to recommend smartphones
    def RecommendSmartphones(self,recommend_input):
        print(type(recommend_input))
        major_recommendation = self.classifier.predict(recommend_input)
        max_val = major_recommendation.max(axis = 1)
        result = nmp.where(major_recommendation == max_val)
        recommended_phone = self.y.columns[nmp.asscalar(result[1])]
        return recommended_phone
    
        
    def Recommend(self,recommend_input):
        if(self.system_trained):
         return   self.RecommendSmartphones(recommend_input)
        
        else:
            self.TrainRecommendationSystem()
            return self.RecommendSmartphones(recommend_input)

            
